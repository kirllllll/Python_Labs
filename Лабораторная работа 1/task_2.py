# TODO Найдите количество книг, которое можно разместить на дискете
disc_vol_mb = 1.44
num_p = 100
num_l = 50
num_s = 25
s_vol = 4

disc_vol_b = disc_vol_mb * 1024 * 1024
book_vol_b = num_p * num_l * num_s * s_vol
book_quantity = disc_vol_b // book_vol_b
print("Количество книг, помещающихся на дискету:", int(book_quantity))
