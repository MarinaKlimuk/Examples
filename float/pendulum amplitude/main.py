start = float(input('Enter an initial amplitude: '))
stop = float (input('Enter a stop amplitude: '))
count = 0

while start - stop > 1e-15:
  start = start - start*0.084
  count += 1
print('The pendulum will stop after {0} oscillations'.format(count))