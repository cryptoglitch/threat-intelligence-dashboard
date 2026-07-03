from rich.console import Console
from rich.table import Table

from ioc_checker import check_ip

console = Console()


def get_risk_display(risk_level):
    """
    Returns a colored risk label.
    """

    colors = {
        "Low": "[green]🟢 Low[/green]",
        "Medium": "[yellow]🟡 Medium[/yellow]",
        "High": "[bright_red]🟠 High[/bright_red]",
        "Critical": "[bold red]🔴 Critical[/bold red]"
    }

    return colors.get(risk_level, risk_level)


console.print("\n[bold cyan]Threat Intelligence Dashboard[/bold cyan]\n")

ip = input("Enter an IP address: ")

try:

    result = check_ip(ip)

    table = Table(title="Threat Intelligence Results")

    table.add_column("Field", style="cyan", width=18)
    table.add_column("Value", style="green")

    table.add_row("IP Address", result["ip"])
    table.add_row("Country", result["country"])
    table.add_row("ISP", result["isp"])
    table.add_row("Domain", result["domain"])
    table.add_row("Abuse Score", str(result["score"]))
    table.add_row("Risk Level", get_risk_display(result["risk_level"]))
    table.add_row("Reports", str(result["reports"]))
    table.add_row("Whitelisted", str(result["whitelisted"]))

    console.print(table)

except Exception as error:

    console.print(f"[bold red]Error:[/bold red] {error}")