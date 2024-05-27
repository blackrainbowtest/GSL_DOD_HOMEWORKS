Task 1
Given a list of integers nums and an integer target, return the indices of the two numbers such that they add up to the target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Example:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Տրված են ամբողջ թվերի (integer) զանգվածը և ամբողջ թիվ ներկայացնող թիրախը (target), վերադարձրեք այն երկու թվերի ինդեքսները, որոնց գումարը հավասար կլինի թիրախին (target):
Խնդրում եմ հաշվի առնել, որ յուրաքանչյուր մուտքագրում կունենա ճիշտ մեկ լուծում, և դուք չեք կարող օգտագործել նույն տարրը երկու անգամ:
Պատասխանը կարող եք վերադարձնել ցանկացած հերթականությամբ։
Օրինակ՝
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Բացատրություն: nums[0] + nums[1] == 9, we return [0, 1].


Task 2
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
Example:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Տրված է ամբողջ թվերով (integer) զանգված, գտեք այդ զանգվածի մաս կազմող այն ենթազանգվածը (որը պարունակում է առնվազն մեկ թիվ), որն ունի ամենամեծ գումարը և վերադարձրեք դրա գումարը:
Օրինակ՝
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Բացատրություն: [4,-1,2,1] ենթազանգվածը ունի ամենամեծ գումարը, որի արժեքը 6 է:
