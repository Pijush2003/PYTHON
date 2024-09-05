courses = ['math', 'physics', 'chemistry', 'biology']
nums=[1,9,5,6,8,2]
# courses_2=['economy','agriculture','nutrition']
# courses.append('bengali')
# courses.extend(courses_2)

# courses.remove('biology')

# popped=courses.pop()
# print(popped)

# courses.reverse()

# courses.sort()

# sorted_courses=sorted(courses)
# print(sorted_courses)
# print(min(nums))
# print(sum(nums))

# print(courses.index('biology'))
# print('Art' in courses)


# for item in courses:
# for index, item in enumerate(courses, start=1):
#     print(index,item)

course_str=','.join(courses)
new_list=course_str.split(' - ')
print(course_str)
print(new_list)