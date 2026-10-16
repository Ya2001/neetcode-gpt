import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        
        x = z - max(z)
        y = sum(np.exp(x))
        your_answer = (np.exp(x)/y) 
        return np.round(your_answer, 4)
        
