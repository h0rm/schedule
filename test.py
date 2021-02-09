import schedule

schedule.every(1).steps.do(lambda: print(f'every step @ {schedule.steps}'))
schedule.every(3).steps.do(lambda: print(
    f'3 step @ {schedule.steps}')).tag('3 step')

for i in range(10):
    schedule.step()
    if i == 6:
        print('cancel 3 step')
        schedule.clear('3 step')
