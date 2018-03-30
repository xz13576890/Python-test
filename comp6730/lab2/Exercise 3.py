canberra_population = c_p = 196037
canberra_families = c_f = 50352
canberra_couple_families = c_c_f = 22850
canberra_single_families = c_s_f = 7243
#people_per_household = p_p_h = canberra_population / canberra_families


canberra_children = c_c =(c_c_f+c_s_f)*1.8
canberra_single_adults = c_s_a = c_p - c_c_f * 2 - c_s_f * 1 - c_c

#print(p_p_h)
print(c_s_a)


