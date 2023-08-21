'''
Creating an optimal order of the times and calculation of a total time and an average time
'''
def getAverageTime(times):
    sorted_times = sorted(times)
    print("Optimal order of times:",sorted_times)
    time_client, sum_times = 0.00, 0.00
    for t in sorted_times:
        time_client += t
        print("time_client =",time_client)
        sum_times += time_client
    print("Time total:", sum_times)
    return sum_times/len(times)

array_times = [1,10,8]
print("for array times is %s, average time is %f" %
      (array_times, getAverageTime(array_times)))

