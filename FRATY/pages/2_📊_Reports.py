import smartpy as sp


@sp.module
def main():
    class StoreValue(sp.Contract):
        def __init__(self, value):
            self.data.storedValue = value

        @sp.entrypoint
        def replace(self, params):
            self.data.storedValue = params.value

        @sp.entrypoint
        def double(self):
            self.data.storedValue *= 2

        @sp.entrypoint
        def divide(self, params):
            assert params.divisor > 5
            self.data.storedValue /= params.divisor


if "main" in __name__:

    @sp.add_test()
    def test():
        scenario = sp.test_scenario("StoreValue", main)
        scenario.h1("Store Value")
        
        c1 = main.StoreValue(0)
        scenario += c1

        c1.replace(value=1)

        
        c1.double()
        c1.double()
        scenario.p("Some computation").show(c1.data.storedValue * 12)
        c1.replace(value=25)
        c1.double()
        scenario.verify(c1.data.storedValue == 50)
        c1.divide(divisor=6)
        scenario.verify(c1.data.storedValue == 8)
