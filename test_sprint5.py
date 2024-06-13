robots = '3 2 2 2 4 5 8 1'
weight_limit = 3

# robots_list = list(map(int, input().split()))


def platform(robots, weight_limit):
    robots_list = sorted(list(map(int, robots.split())))
    platform_count = 0
    left = 0
    right = len(robots_list) - 1

    # for i in robots_list:
    #     if i == weight_limit:
    #         platform_count += 1

    while left <= right:
        # if robots_list[right] == robots_list[left]:
        #     break

        if robots_list[left] + robots_list[right] <= weight_limit:
            left += 1
            right -= 1
            platform_count += 1

        # else:
        #     right -= 1

            # platform_count += 1

    return platform_count


print(platform(robots, weight_limit))
