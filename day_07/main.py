from collections import defaultdict
from copy import deepcopy

data = [i.strip() for i in open('input').readlines()]

if __name__ == "__main__":
    instructions = defaultdict(list)
    order = ""
    for i in range(26):
        instructions[chr(ord('A') + i)]
    for line in data:
        step = line.split(" ")[7]
        previous_step = line.split(" ")[1]
        instructions[step].append(previous_step)
    for entry in instructions:
        instructions[entry] = sorted(instructions[entry])
    instructions2 = deepcopy(instructions)

    while instructions:
        # find first element with len(value) = 0
        for entry in instructions:
            if len(instructions[entry]) == 0:
                current_step = entry
                break
        for entry in instructions:
            if current_step in instructions[entry]:
                instructions[entry].remove(current_step)
        order += current_step
        instructions.pop(current_step)
    print("Ordered instruction: {:s}".format(order))
    print("-------------------------")

    time = 0
    workers = [{"time": 0, "step": None} for _ in range(5)]

    while instructions2 or any(worker["time"] > 0 for worker in workers):
        current_steps = []
        worker_steps = [worker["step"] for worker in workers]

        for entry in instructions2:
            if len(instructions2[entry]) == 0 and entry not in worker_steps:
                current_steps.append(entry)
            if len(current_steps) == 5:
                break

        for worker in workers:
            worker["time"] = max(worker["time"] - 1, 0)
            if worker["time"] == 0:
                if worker["step"] is not None:
                    for entry in instructions2:
                        if worker["step"] in instructions2[entry]:
                            instructions2[entry].remove(worker["step"])
                    instructions2.pop(worker["step"])
                    worker["step"] = None
                if current_steps:
                    worker["step"] = current_steps.pop()
                    worker["time"] += 60 + ord(worker["step"]) - ord('A')
        time += 1
    print("Time to complete all steps: {:d}".format(time))