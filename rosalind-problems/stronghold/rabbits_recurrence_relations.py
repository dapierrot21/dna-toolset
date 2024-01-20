def rabbit_recurrence_relations(months, offsprings):
    """Fibonacci Loop"""
    parent, child = 1, 1
    for _ in range(months - 1):
        child, parent = parent, parent + (child * offsprings)
    return child


print(rabbit_recurrence_relations(32, 4))


# o - small (children) rabbits. They have to mature and reproduce in the next cycleonly.
# 0 - mature (adults) rabbits. They can reproduce and move to the next cycle.

# Month 1: [o]
# Month 2: [0]
# Month 3: [0 o o]
# Month 4: [0 o o 0 0]
# Month 5: [0 o o 0 0 0 o o 0 o o]
