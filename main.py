"""CLI entrypoint for the single-agent project."""

from argparse import ArgumentParser, Namespace

from single_agent.agent.bootstrap import bootstrap_report
from single_agent.config.settings import get_settings
from single_agent.utils.logging import setup_logging


def build_parser() -> ArgumentParser:
    """Build command line parser for supported commands."""
    parser = ArgumentParser(description="Single-agent CLI")
    parser.add_argument(
        "command",
        choices=["bootstrap"],
        help="Command to execute",
    )
    return parser


def run_bootstrap() -> int:
    """Run the initial bootstrap command."""
    settings = get_settings()
    setup_logging(settings.run.log_level)

    report = bootstrap_report(settings)
    print("Bootstrap OK")
    print(f"IMAP Host: {report.imap_host}")
    print(f"Mailbox: {report.mailbox}")
    print(f"Days Back: {report.days_back}")
    print(f"Max Emails: {report.max_emails}")
    return 0


def main() -> int:
    """Main command dispatcher."""
    parser = build_parser()
    args: Namespace = parser.parse_args()

    if args.command == "bootstrap":
        return run_bootstrap()

    parser.error("Unsupported command")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
