m = float(input('Digite um valor em metros:'))
cm = m*100
mm = m*1000
dm = m*10
km = m/1000
hm = m/100
dam = m/10
print('{:.1f}m, corresponde a {:.0f}dm, {:.0f}cm e {:.0f}mm.'.format(m, dm, cm, mm))
print('{:.1f}m, vale {}km, {}hm e {}dam.'.format(m, km, hm, dam))
