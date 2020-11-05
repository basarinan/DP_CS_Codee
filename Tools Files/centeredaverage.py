def centered_average(nums):
  total = 0
  nums.sort()
  for i in range(len(nums)):
    total = total + 1
  average = total / 2
  if total % 2 == 0:
    yup = average - 1
    cenaverage = (nums[int(average)] + nums[int(yup)]) /2
    print(cenaverage)
    exit()
  if total % 2 != 0:
    average = average + 0.5
    average = average -1
    
    t = (nums[int(average)])
    print(t)

   

centered_average([589,589.5,583.5])
