# Type your code here


print("Davy's auto shop services")
service = {"Oil change":35,"Tire rotation":19,"Car wash":7,"Car wax":12}
for service_name,service_price in service.items():
    print("{0} -- ${1}".format(service_name,service_price))
print()
first_service = input("Select first service:\n")
second_service = input("Select second service:\n")

if first_service=='-':
    # price_first = service[first_service]
    price_first = 0
    first_service="No service"
else:
    price_first = service[first_service]

if second_service=='-':
    # 
    price_second = 0
    second_service="No service"
else:
    price_second = service[second_service]
    
    
total = price_first+price_second
print()
print("Davy's auto shop invoice\n")
if first_service!="No service":
    print("Service 1: {0}, ${1}".format(first_service,service[first_service]))
else:
    print("Service 1: {0}".format(first_service))
    
if second_service!="No service":
    print("Service 2: {0}, ${1}".format(second_service,service[second_service]))
else:
    print("Service 2: {0}".format(second_service))

print()

print("Total: ${0}".format(total))
