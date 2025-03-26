from typing import Optional
from pydantic import BaseModel


class CardTransaction(BaseModel):
    amount: Optional[float]
    currency: Optional[str]
    transaction_type: Optional[str]
    country: Optional[str]
    city: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]
    timezone: Optional[str]
    device_type: Optional[str]
    operating_system: Optional[str]
    app_version: Optional[str]
    avg_spend_30d: Optional[float]
    transactions_last_7d: Optional[int]
    time_since_last_login: Optional[float]
    login_attempts_last_24h: Optional[int]
    is_new_device: Optional[int]
    vpn_usage: Optional[int]
    proxy_usage: Optional[int]
    ip_risk_score: Optional[int]
    ISP: Optional[str]
