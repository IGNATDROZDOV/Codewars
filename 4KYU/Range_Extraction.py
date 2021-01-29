def solution(args):
    output = []
    i = 0
    while(True):
        if len(args) == 0:
            return ",".join(output)
        if len(args) == 1:
            output.append(str(args[-1]))
            return ",".join(output)
        if len(args) == 2:
            output.append(str(args[-2]))
            output.append(str(args[-1]))
            return ",".join(output)
        else:
            max_count = 0
            if args[i] + 2 == args[i + 2]:
                start_pos = i
                max_count = i + 2
                if i + 3 < len(args):
                    while(args[i + 2] == args[i + 3] - 1):
                        if i + 4 < len(args):
                            max_count += 1
                            i += 1
                        elif args[i + 2] == args[i + 3] - 1:
                            max_count += 1
                            i+=1
                            break
                else:
                    output.append('{}-{}'.format(args[start_pos], args[max_count]))
                    return ",".join(output)
                output.append('{}-{}'.format(args[start_pos], args[max_count]))
                args = args[max_count+1:]    
                i = 0
            elif args[i] + 2 != args[i + 2]:
                output.append(str(args.pop(i)))
                i = 0