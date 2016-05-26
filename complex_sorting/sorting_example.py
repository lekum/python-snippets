employees = [{"name" : "mary",
              "age": 23,
              "salary": 16000,
             },
             {"name" : "john",
              "age": 35,
              "salary": 48000,
             },
             {"name" : "mark",
              "age": 21,
              "salary": 48000,
             },
             {"name" : "markII",
              "age": 22,
              "salary": 48000,
             },
             {"name" : "sarah",
              "age": 44,
              "salary": 55000,
             }]

# Sort by age descending
employees.sort(key=lambda x: x["age"], reverse=True)

# Sort by salary ascending
employees.sort(key=lambda x: x["salary"])
print(employees)
