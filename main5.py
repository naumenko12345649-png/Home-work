m_list = [0, 1, 7, 2, 4, 8]
if not m_list:
    result = 0
else:
    even_sum = 0
    for i, val in enumerate(m_list):
        if i % 2 == 0:
            even_sum += val

    result = even_sum * m_list[-1]
print(result)

m_list = [1, 3, 5]
if not m_list:
    result = 0
else:
    even_sum = 0
    for i, val in enumerate(m_list):
        if i % 2 == 0:
            even_sum += val

    result = even_sum * m_list[-1]
print(result)

m_list = [6]
if not m_list:
    result = 0
else:
    even_sum = 0
    for i, val in enumerate(m_list):
        if i % 2 == 0:
            even_sum += val

    result = even_sum * m_list[-1]
print(result)

m_list = []
if not m_list:
    result = 0
else:
    even_sum = 0
    for i, val in enumerate(m_list):
        if i % 2 == 0:
            even_sum += val

    result = even_sum * m_list[-1]
print(result)

