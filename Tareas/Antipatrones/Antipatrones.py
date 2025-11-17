import json
from pathlib import Path

# Correccion del antipatron Magic Numbers
# Valores sin contexto, pasan a tener nombres descriptivos.
GoldMinTotal= 100
GoldDiscount = 0.15

SilverMinTotal= 42
SilverDiscount = 0.07

BaseDomestic = 5
BaseInternational = 7

WeightFactor = 0.25
Distance = 300

HeavyThreshold = 20
HeavyFeeDomestic = 3
HeavyFeeInternational = 4

DefaultTotal = 123.45
DefaultWeight = 12
DefaultDistance = 900

# Solucion para God Object
# Una clase con demasiada lógica, se hace una separacion por responsabilidad.
class UserRepository:
    def __init__(self, db_path="data.json"):
        self.db_path = Path(db_path)

    def load_users(self):
        if not self.db_path.exists():
            return []
        return json.loads(self.db_path.read_text(encoding="utf-8"))


class DiscountService:
    def discount_for_order(self, user, total):
        tier = user.get("tier")

        if tier == "gold" and total > GoldMinTotal:
            return total * GoldDiscount

        if tier == "silver" and total > SilverMinTotal:
            return total * SilverDiscount

        return 0.0

# Analisis de Copy-Paste Programming
# Codigo duplicado, buscamos una solucion mas optima unificandolos
class ShippingService:
    def calculate_shipping(self, base, heavy_fee, weight, distance):
        variable = weight * WeightFactor + (distance / Distance)

        if weight > HeavyThreshold:
            variable += heavy_fee

        return base + variable

    def domestic(self, weight, distance):
        return self.calculate_shipping(BaseDomestic, HeavyFeeDomestic, weight, distance)

    def international(self, weight, distance):
        return self.calculate_shipping(BaseInternational, HeavyFeeInternational, weight, distance)



class AppManager:
    def __init__(self):
        self.repo = UserRepository()
        self.discounts = DiscountService()
        self.shipping = ShippingService()

    def print_user(self, user):
        print(f"[{user.get('id')}] {user.get('name')} - tier={user.get('tier')}")

    def run(self):
        users = self.repo.load_users()

        for u in users:
            self.print_user(u)

            d = self.discounts.discount_for_order(u, DefaultTotal)
            print(f"Descuento calculado: {d:.2f}")

            print("Envío nacional:", self.shipping.domestic(DefaultWeight, DefaultDistance))
            print("Envío internacional:", self.shipping.international(DefaultWeight, DefaultDistance))


if __name__ == "__main__":
    AppManager().run()
