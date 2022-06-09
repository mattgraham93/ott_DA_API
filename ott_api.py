import pandas as pd
import scipy.stats as st

class Probability:
    class Poisson():
        # def __init__(self, name: str) -> object:
        #     print(f"Making distribution")
        #     self.name = name
        #     self.dist = s
        #     print(f"Created")

        def get_dist(self, mu, n):
            return st.poisson.rvs(mu=mu, size=n)  # getting random poisson distribution

        def get_prob(sel: float, mu: float):
            # print(f"Get probability")
            return st.poisson.pmf(sel, mu)

    class Normal():
        def get_dist(self, ):
            return st.norm.rvs(mu=0.6, size=1000)  # getting random poisson distribution

        def get_prob(sel: float, mu: float):
            print(f"Get probability")
            return st.norm.pmf(sel, mu)

            
# class Tests:
#     def t_test():
#         print(f"T test")

#     def z_test():
#         print(f"Z test")


def main():
    pois_dist = Probability.Poisson().get_dist(5, 1000)
    print(pois_dist)  # this is the acual distribution, a list
    my_prob = Probability.Poisson.get_prob(sel = 3, mu = 4)
    print(my_prob)  # get probability of selection and expected mean


if __name__ == "__main__":
    main()