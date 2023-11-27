import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

# Parameters for the prior beta distribution
alpha_prior, beta_prior = 2, 2

# Data from the first screening
likes_first_screening, total_first_screening = 50, 60

# Data from the second screening
dislikes_second_screening, total_second_screening = 34, 50

# Prior distribution
x = np.linspace(0, 1, 1000)
prior_distribution = beta.pdf(x, alpha_prior, beta_prior)

# Posterior distribution after the first screening
alpha_posterior_first = alpha_prior + likes_first_screening
beta_posterior_first = beta_prior + (total_first_screening - likes_first_screening)
posterior_distribution_first = beta.pdf(x, alpha_posterior_first, beta_posterior_first)

# Posterior distribution after the second screening
alpha_posterior_second = alpha_posterior_first + total_second_screening - dislikes_second_screening
beta_posterior_second = beta_posterior_first + (dislikes_second_screening)
posterior_distribution_second = beta.pdf(x, alpha_posterior_second, beta_posterior_second)


# Plot for the prior distribution
plt.subplot(3, 1, 1)
plt.plot(x, prior_distribution, label='Prior (Beta(2, 2))')
plt.title('Prior Distribution')
plt.legend()

# Plot for the posterior distribution after the first screening
plt.subplot(3, 1, 2)
plt.plot(x, posterior_distribution_first, label='Posterior after First Screening')
plt.title('Posterior Distribution after First Screening')
plt.legend()

# Plot for the posterior distribution after the second screening
plt.subplot(3, 1, 3)
plt.plot(x, posterior_distribution_second, label='Posterior after Second Screening')
plt.title('Posterior Distribution after Second Screening')
plt.legend()

plt.tight_layout()
plt.show()