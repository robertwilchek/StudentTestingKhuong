
def log_event(event, events=[]):
    events.append(event)
    return events


if __name__ == "__main__":
    # Take returned list
    e = log_event("start")
    # Print list
    print(e)
    # Pop added value
    e.pop()
    # Add and print list
    print(log_event("next", e))       