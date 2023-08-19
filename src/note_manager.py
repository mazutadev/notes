class NoteManager:
    @staticmethod
    def add(instance, item):
        if len(instance.data_list) > 0:
            uid = max(instance.data_list.keys()) + 1
            instance.uid = uid
            instance.data_list[uid] = item
        else:
            instance.uid = 0
            instance.data_list[0] = item

    @staticmethod
    def remove(instance, uid):
        if uid in instance.data_list:
            del instance.data_list[uid]
        else:
            raise Exception(f"Объекта с id {uid} не найдено")

    @staticmethod
    def get(instance, uid):
        if uid in instance.data_list:
            return instance.data_list[uid]
