import aiohttp


class GetRequests:
    def __init__(self):
        self.url = 'http://127.0.0.1:8000/api/v1/'

    async def get_user(self, user_id):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.url + f'users/{user_id}/') as response:
                    if response.status == 200:
                        return True
                    elif response.status == 404:
                        return False
                    else:
                        print(f"{response.status}")
                        return None
        except aiohttp.ClientError as e:
            print(f"{e}")
            return None

    async def create_user(self, user_id, username, first_name):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(self.url + 'users/',
                                        json={"telegram_id": user_id, "username": username,
                                              "first_name": first_name}) as response:
                    if response.status == 201:
                        return await response.json()
                    elif response.status == 404:
                        print(f"{response.status}")
                        return None
        except aiohttp.ClientError as e:
            print(f" {e}")
            return None

    async def update_language(self, user_id, language):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.patch(self.url + f'users/{user_id}/',
                                         json={"language": language}) as response:
                    if response.status == 200:
                        return True
                    elif response.status == 404:
                        print(f"Malumotlar toplmadi {user_id}")
                        return False
                    else:
                        print(f"{response.status}")
                        return None
        except aiohttp.ClientError as e:
            print(f"{e}")
            return None

    async def get_language_by_user_id(self, user_id):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.url + f'users/{user_id}/') as response:
                    if response.status == 200:
                        data = await response.json()
                        return data.get('language')
                    elif response.status == 404:
                        print(f"Malumotlar toplmadi {user_id}")
                        return None
                    else:
                        print(f" {response.status}")
                        return None
        except aiohttp.ClientError as e:
            print(f" {e}")
            return None

    async def registration_user(self, user_id):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.url + f'users/{user_id}/') as response:
                    if response.status == 200:
                        data = await response.json()
                        return data.get('ism_fam'), data.get('phone_number'),
                    elif response.status == 404:
                        print(f"Malumotlar toplmadi {user_id}")
                        return None
                    else:
                        print(f" {response.status}")
                        return None
        except aiohttp.ClientError as e:
            print(f" {e}")
            return None

    async def patch_user_full_name_username(self, user_id, foydaluvchi_ism_fam, foydaluvchi_tel):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.patch(self.url + f'users/{user_id}/',
                                         json={"ism_fam": foydaluvchi_ism_fam,
                                               "phone_number": foydaluvchi_tel}) as response:
                    if response.status == 200:
                        return True
                    elif response.status == 404:
                        print(f"Malumotlar toplmadi {user_id}")
                        return False
                    else:
                        print(f"{response.status}")
                        return None
        except aiohttp.ClientError as e:
            print(f" {e}")
            return None

    async def get_is_active_by_user_id(self, user_id):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.url + f'users/{user_id}/') as response:
                    if response.status == 200:
                        data = await response.json()
                        return data.get('is_active')
                    elif response.status == 404:
                        print(f"Malumotlar toplmadi {user_id}")
                        return None
                    else:
                        print(f"{response.status}")
                        return None
        except aiohttp.ClientError as e:
            print(f" {e}")
            return None

    async def get_is_tarif_by_user_id(self, user_id):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.url + f'users/{user_id}/') as response:
                    if response.status == 200:
                        data = await response.json()
                        return data.get('user_tarif')
                    elif response.status == 404:
                        print(f"Malumotlar toplmadi {user_id}")
                        return None
                    else:
                        print(f"{response.status}")
                        return None
        except aiohttp.ClientError as e:
            print(f" {e}")
            return None

    async def patch_user_is_activate(self, user_id, is_actiavte):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.patch(self.url + f'users/{user_id}/',
                                         json={"is_active": is_actiavte}) as response:
                    if response.status == 200:
                        return True
                    elif response.status == 404:
                        print(f"Malumotlar toplmadi {user_id} ")
                        return False
                    else:
                        print(f" {response.status}")
                        return None
        except aiohttp.ClientError as e:
            print(f"{e}")
            return None

    async def get_categories(self):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.url + f'tarif/') as response:
                    if response.status == 200:
                        return await response.json()
                    elif response.status == 404:
                        return False
                    else:
                        print(f"Sorovda xatolik {response.status}")
                        return None
        except aiohttp.ClientError as e:
            print(f" {e}")
            return None

    async def select_category_by_id(self, category_id):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.url + f'tarif/{category_id}/') as response:
                    if response.status == 200:
                        return await response.json()
                    elif response.status == 404:
                        return False
                    else:
                        print(f"Sorovda xatolik {response.status}")
                        return None
        except aiohttp.ClientError as e:
            print(f"{e}")
            return None

    async def patch_user_tarif_name(self, user_id, user_tarif):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.patch(self.url + f'users/{user_id}/',
                                         json={"user_tarif": user_tarif}) as response:
                    if response.status == 200:
                        return True
                    elif response.status == 404:
                        print(f"{user_id} ga tegishli malumotlar toplmadi.")
                        return False
                    else:
                        print(f"{response.status}")
                        return None
        except aiohttp.ClientError as e:
            print(f"{e}")
            return None

    async def update_datetime_start(self, user_id, start_date, future_date, end_date):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.patch(self.url + f'users/{user_id}/',
                                         json={"active_tarif_user_start": start_date,
                                               'active_tarif_user_end': future_date,
                                               'tarif_end': end_date}) as response:
                    if response.status == 200:
                        return True
                    elif response.status == 404:
                        print(f"{user_id} ga tegishli malumotlar toplmadi")
                        return False
                    else:
                        print(f"{response.status}")
                        return None
        except aiohttp.ClientError as e:
            print(f" {e}")
            return None

    async def update_day_users(self, user_id, remain_days):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.patch(self.url + f'users/{user_id}/',
                                         json={'tarif_end': remain_days}) as response:
                    if response.status == 200:
                        return True
                    elif response.status == 404:
                        print(f"Malumotlar toplmadi {user_id}.")
                        return False
                    else:
                        print(f"{response.status}")
                        return None
        except aiohttp.ClientError as e:
            print(f"{e}")
            return None

    async def get_all_user_information(self, user_id):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.url + f'users/{user_id}/') as response:
                    if response.status == 200:
                        return await response.json()
                    elif response.status == 404:
                        return False
                    else:
                        print(f"Foydalanuvchi topilmadi: {response.status}")
                        return None
        except aiohttp.ClientError as e:
            print(f"{e}")
            return None

    async def get_tarif_users(self, user_id):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.url + f'users/{user_id}/') as response:
                    if response.status == 200:
                        data = await response.json()
                        return data.get('active_tarif_user_start'), data.get('active_tarif_user_end'), data.get(
                            'tarif_end')
                    elif response.status == 404:
                        print(f"Foydalanuvchi topilmadi{user_id} ")
                        return None, None, None
                    else:
                        print(f"malumotlarni olishda xatolik {response.status}")
                        return None, None, None
        except aiohttp.ClientError as e:
            print(f"tarifni olishda xatolik{e}")
            return None, None, None
