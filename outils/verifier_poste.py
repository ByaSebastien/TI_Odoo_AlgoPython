"""Vérifie que le poste est prêt pour la formation.

Outil fourni par le cours : c'est le seul fichier à copier dans votre projet,
dans un dossier outils/. Il n'est pas nécessaire de comprendre son code pour
l'utiliser. Lancement, depuis le dossier de votre projet :

    uv run python outils/verifier_poste.py

Code de retour : 0 si tout est prêt, 1 sinon. Les outils de développement
(pytest, ruff, mypy) sont seulement signalés : ils s'installent plus tard, au
module qui en a besoin.

Les messages n'utilisent que des caractères affichables même sans mode UTF-8 :
l'outil doit fonctionner justement sur un poste mal configuré.
"""

import importlib.util
import sys

REQUIRED_VERSION = (3, 14)
# Outil -> module du cours où on l'installe.
LATER_TOOLS = {"pytest": "08", "ruff": "13", "mypy": "13"}
EXIT_SUCCESS = 0
EXIT_FAILURE = 1


def is_python_version_ok() -> bool:
    """Indique si la version de Python est au moins REQUIRED_VERSION."""
    return sys.version_info >= REQUIRED_VERSION


def is_virtual_environment_active() -> bool:
    """Indique si le script s'exécute dans un environnement virtuel."""
    return sys.prefix != sys.base_prefix


def is_utf8_mode_enabled() -> bool:
    """Indique si le mode UTF-8 de Python est actif (ou inutile hors Windows)."""
    return sys.platform != "win32" or sys.flags.utf8_mode == 1


def is_installed(tool: str) -> bool:
    """Indique si un outil (un paquet Python) est installé dans l'environnement."""
    return importlib.util.find_spec(tool) is not None


def main() -> int:
    """Lance les vérifications et affiche un conseil pour chaque échec."""
    major, minor = REQUIRED_VERSION
    checks = [
        (
            f"Python {major}.{minor} ou plus",
            is_python_version_ok(),
            "Installez Python avec : uv python install 3.14",
        ),
        (
            "Environnement virtuel du projet actif",
            is_virtual_environment_active(),
            "Lancez ce script avec « uv run », depuis le dossier de votre projet.",
        ),
        (
            "Mode UTF-8 actif",
            is_utf8_mode_enabled(),
            "Créez la variable d'environnement PYTHONUTF8=1 (module 00, section 3).",
        ),
    ]

    for label, success, advice in checks:
        print(f"[{'OK' if success else 'KO'}] {label}")
        if not success:
            print(f"     -> {advice}")

    for tool, module in LATER_TOOLS.items():
        if is_installed(tool):
            print(f"[OK] {tool} installé")
        else:
            print(f"[..] {tool} pas encore installé (normal avant le module {module})")

    if all(success for _, success, _ in checks):
        print("Le poste est prêt pour la formation.")
        return EXIT_SUCCESS
    print("Le poste n'est pas encore prêt.")
    return EXIT_FAILURE


if __name__ == "__main__":
    sys.exit(main())
