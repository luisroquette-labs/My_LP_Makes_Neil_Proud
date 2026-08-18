#!/usr/bin/env python3
"""Deterministic FORM validation for LpBlueprint JSON (no LLM).

Implements gate 1 (validar-estrutura) from references/criacao/geracao.md:
checks the shape of the JSON — field by field, array element by element.
It does NOT check content quality, SEO lengths, or contrast (gates 2-4 are
instructional and applied by the agent).

Usage:
    python3 scripts/validar-blueprint.py --input examples/example-briefing-input.json
Exit code: 0 = form valid, 1 = form errors found.
"""

import argparse
import json
import sys
from datetime import datetime

MODELOS = {"universal", "curso", "evento", "captura", "squeeze", "lancamento"}
OBJETIVOS = {"captura", "venda"}
TEMAS = {"claro", "escuro"}
COMPRIMENTOS = {"curta", "media", "longa"}
RISCOS = {"baixo", "medio", "alto"}
FORMATOS_EVENTO = {"presencial", "online", "hibrido"}

UNIVERSAL_STRING_FIELDS = ["slug", "modelo", "objetivo", "headline",
                           "subheadline", "publicoAlvo", "tema",
                           "comprimento", "riscoOferta"]


def _parse_iso(value):
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
        return True
    except (ValueError, TypeError, AttributeError):
        return False


def _is_lista_de_strings(value, campo):
    if not isinstance(value, list) or not value:
        return [f"{campo}: must be a non-empty array of strings"]
    errs = []
    for i, item in enumerate(value):
        if not isinstance(item, str):
            errs.append(f"{campo}[{i}]: must be a string")
    return errs


def _is_lista_de_objetos(value, campo, chaves):
    if not isinstance(value, list):
        return [f"{campo}: must be an array of objects"]
    errs = []
    for i, item in enumerate(value):
        if not isinstance(item, dict):
            errs.append(f"{campo}[{i}]: must be an object")
            continue
        for chave in chaves:
            if not isinstance(item.get(chave), str):
                errs.append(f"{campo}[{i}].{chave}: must be a string")
    return errs


def _valida_seo(seo):
    errs = []
    for campo in ("metaTitle", "metaDescription"):
        valor = seo.get(campo)
        if valor is not None and not isinstance(valor, str):
            errs.append(f"seo.{campo}: must be a string")
    return errs


def _valida_visual(visual):
    errs = []
    cores = visual.get("cores")
    if cores is not None:
        if not isinstance(cores, dict):
            return ["visual.cores: must be an object"]
        for campo in ("fundo", "texto", "destaque", "acento"):
            valor = cores.get(campo)
            if valor is not None and not isinstance(valor, str):
                errs.append(f"visual.cores.{campo}: must be a string")
    return errs


def validar(blueprint):
    """Returns a list of form errors. Empty list = valid."""
    errs = []

    if not isinstance(blueprint, dict):
        return ["blueprint: must be a JSON object"]

    # Universal fields: presence + string type.
    for campo in UNIVERSAL_STRING_FIELDS:
        valor = blueprint.get(campo)
        if not isinstance(valor, str) or not valor.strip():
            errs.append(f"{campo}: required non-empty string")

    if blueprint.get("modelo") not in MODELOS:
        errs.append(f"modelo: must be one of {sorted(MODELOS)}")
    if blueprint.get("objetivo") not in OBJETIVOS:
        errs.append(f"objetivo: must be one of {sorted(OBJETIVOS)}")
    if blueprint.get("tema") not in TEMAS:
        errs.append(f"tema: must be one of {sorted(TEMAS)}")
    if blueprint.get("comprimento") not in COMPRIMENTOS:
        errs.append(f"comprimento: must be one of {sorted(COMPRIMENTOS)}")
    if blueprint.get("riscoOferta") not in RISCOS:
        errs.append(f"riscoOferta: must be one of {sorted(RISCOS)}")

    if not isinstance(blueprint.get("evergreen"), bool):
        errs.append("evergreen: required boolean")

    beneficios = blueprint.get("beneficios")
    errs += _is_lista_de_strings(beneficios, "beneficios")

    cta = blueprint.get("cta")
    if not isinstance(cta, dict) or not isinstance(cta.get("texto"), str):
        errs.append("cta: must be an object with a 'texto' string")

    lgpd = blueprint.get("lgpd")
    if not isinstance(lgpd, dict) or lgpd.get("consentimento") is not True:
        errs.append("lgpd: must be an object with consentimento: true")

    # Per-model object: form checks only (mirrors validar-estrutura).
    modelo = blueprint.get("modelo")
    if modelo == "evento":
        evento = blueprint.get("evento")
        if not isinstance(evento, dict):
            errs.append("evento: model 'evento' requires the 'evento' object")
        else:
            if not isinstance(evento.get("dataInicio"), str) or not _parse_iso(evento.get("dataInicio")):
                errs.append("evento.dataInicio: required parseable ISO date")
            if evento.get("formato") not in FORMATOS_EVENTO:
                errs.append(f"evento.formato: must be one of {sorted(FORMATOS_EVENTO)}")
            errs += _is_lista_de_strings(evento.get("beneficiosParticipar"), "evento.beneficiosParticipar")
            if evento.get("agenda") is not None:
                errs += _is_lista_de_objetos(evento.get("agenda"), "evento.agenda", ("horario", "titulo"))
            if evento.get("palestrantes") is not None:
                errs += _is_lista_de_objetos(evento.get("palestrantes"), "evento.palestrantes", ("nome", "papel"))
            formato = evento.get("formato")
            if formato in ("presencial", "hibrido") and not isinstance(evento.get("local"), str):
                errs.append("evento.local: required string for presencial/hibrido")
            if formato in ("online", "hibrido") and not isinstance(evento.get("acesso"), str):
                errs.append("evento.acesso: required string for online/hibrido")

    elif modelo == "captura":
        captura = blueprint.get("captura")
        if not isinstance(captura, dict):
            errs.append("captura: model 'captura' requires the 'captura' object")
        else:
            recompensa = captura.get("recompensa")
            if not isinstance(recompensa, dict):
                errs.append("captura.recompensa: must be an object")
            else:
                for campo in ("tipo", "titulo", "descricao"):
                    if not isinstance(recompensa.get(campo), str):
                        errs.append(f"captura.recompensa.{campo}: must be a string")
            errs += _is_lista_de_strings(captura.get("entregaveis"), "captura.entregaveis")

    elif modelo == "lancamento":
        lancamento = blueprint.get("lancamento")
        if not isinstance(lancamento, dict):
            errs.append("lancamento: model 'lancamento' requires the 'lancamento' object")
        else:
            if not isinstance(lancamento.get("nomeProduto"), str) or not lancamento.get("nomeProduto").strip():
                errs.append("lancamento.nomeProduto: required non-empty string")
            if not isinstance(lancamento.get("dataLancamento"), str) or not _parse_iso(lancamento.get("dataLancamento")):
                errs.append("lancamento.dataLancamento: required parseable ISO date")

    # Optional sections: absent is OK (omitted, not zero), wrong shape is not.
    if blueprint.get("seo") is not None:
        if isinstance(blueprint.get("seo"), dict):
            errs += _valida_seo(blueprint["seo"])
        else:
            errs.append("seo: must be an object when present")
    if blueprint.get("visual") is not None:
        if isinstance(blueprint.get("visual"), dict):
            errs += _valida_visual(blueprint["visual"])
        else:
            errs.append("visual: must be an object when present")

    return errs


def main():
    parser = argparse.ArgumentParser(description="Validate LpBlueprint JSON form.")
    parser.add_argument("--input", required=True, help="Path to blueprint JSON.")
    args = parser.parse_args()

    with open(args.input, encoding="utf-8") as f:
        blueprint = json.load(f)

    errs = validar(blueprint)
    if errs:
        print(f"FORM INVALID ({len(errs)} error(s)):")
        for e in errs:
            print(f"  - {e}")
        sys.exit(1)

    print(f"FORM VALID — modelo={blueprint.get('modelo')}")
    sys.exit(0)


if __name__ == "__main__":
    main()
