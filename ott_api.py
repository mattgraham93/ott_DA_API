import pandas as pd
import scipy.stats as st

class Probability:
    class Poisson():
        def __init__(self, name: str) -> object:
            print(f"Making distribution")
            self.name = name
            self.dist = st.poisson.rvs(mu=0.6, size=1000)  # getting random poisson distribution
            print(f"Created")

        def get_prob(sel: float, mu: float):
            print(f"Get probability")
            return st.poisson.pmf(k, mu)

#     class Normal():
#         print(f"Normal")

#         def get_prob():
#             print(f"Get probability")

            
# class Tests:
#     def t_test():
#         print(f"T test")

#     def z_test():
#         print(f"Z test")


def main():
    pois = Probability.Poisson(name="Poisson")
    print(pois.dist)  # this is the acual distribution, a list

    pois.get_prob(3, 4)


if __name__ == "__main__":
    main()