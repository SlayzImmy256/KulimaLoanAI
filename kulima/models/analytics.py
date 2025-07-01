from typing import List, Dict, Any

class Dashboard:
    def __init__(self, farmer_id: str, loan_data: List[Dict[str, Any]], weather_alerts: List[str]):
        self.farmer_id = farmer_id
        self.loan_data = loan_data
        self.weather_alerts = weather_alerts

    def render_visuals(self):
        pass

    def export_data(self, format: str = 'csv'):
        pass

class ReportGenerator:
    def __init__(self, time_period: str, metrics: List[str]):
        self.time_period = time_period
        self.metrics = metrics

    def create_loan_report(self):
        pass

    def send_to_stakeholders(self, report: Any):
        pass 