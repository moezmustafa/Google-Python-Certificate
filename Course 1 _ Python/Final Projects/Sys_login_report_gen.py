def get_event_date(event):
    return event.date()

def current_users(event):
    return event.sort(key=get_event_date)
    machine = {}
    for event in events:
        if event.machine not in machine:
            machine[event.machine] = set()

        if event.type == "login":
            machine[event.machine].add(event.user)
        elif event.type == "logout":
            machine[event.machine].remove(event.user)
        
    return machines

def generate_report(events):
    for machine, users in current_users(events).items():
        if len(users) > 0:
            user_list = ", ".join(users)
            print("{}: {}".format(machine, user_list))