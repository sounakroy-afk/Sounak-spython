import numpy as np

# Two force vectors acting on a 2D particle
v1 = np.array([3.0, 4.0])  # Force 1
v2 = np.array([-2.0, 5.0])  # Force 2
v_net = v1 + v2
print(v_net)
v1_scaled = v1 * 2
v2_scaled = v2 * -1
net_magnitude = np.linalg.norm(v_net)
print(net_magnitude)
