class DbRouter(object):
    """
    Controlamos desde que base de datos obtenemos los datos, pero siempre escribimos
    en la base de datos por defecto
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read auth models go to auth_db.
        """
        if model._meta.app_label == 'ctactecli':
            return 'firebird'
        return None

    """
    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'ctactecli':
            return 'firebird'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'ctactecli' or \
           obj2._meta.app_label == 'ctactecli':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'ctactecli':
            return db == 'firebird'
        return None
    """