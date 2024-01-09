from repository.data_repo import CustomerRepo, CookedDishRepo, DrinkRepo, OrderRepo


def display_data(repo_type):
    types = {
        0: CookedDishRepo,
        1: DrinkRepo,
        2: CustomerRepo,
        3: OrderRepo
    }

    repo = types[repo_type]()

    list = repo.load()
    if list:
        for index in range(len(list)):
            print(index, str(list[index]))
    print('\n')