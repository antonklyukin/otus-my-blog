from .setup_db import delete_db_file, prepare_session, populate_db

if __name__ == '__main__':
    delete_db_file()
    session = prepare_session()
    populate_db(session())
    print('OK!')
