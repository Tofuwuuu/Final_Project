from views import init_app
import models.setup.init_db as dbsetup
if __name__ == "__main__":
    if(dbsetup.initialize_database()):
        print("Database initialization completed successfully.")
        init_app.init.mainloop() # Runner file for the main_init app. Do not modify unless required.        