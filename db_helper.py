import psycopg2


class DbHelper:

	def __init__(self):
		
		try:
			self.connection = psycopg2.connect(user="haseeb", password="12345", host="127.0.0.1", port="5432", database="fourchanthreads")
			self.cursor = self.connection.cursor()
		except (Exception, psycopg2.Error) as error:
			print("Failed to connect", error)

	def insert_thread(self, thread_name, board_name, thread_id):
		row_id = 0

		postgres_insert_query = """ INSERT INTO threads (name, board_name, fourchan_thread_id) VALUES (%s,%s,%s) RETURNING id;"""
		record_to_insert = (thread_name, board_name, thread_id)

		try:
			self.cursor.execute(postgres_insert_query, record_to_insert)	
		except Exception as e:
			self.connection.rollback()
		else:
			self.connection.commit()
			row_id = self.cursor.fetchone()[0]
			print (row_id, "Thread inserted successfully.")
		return row_id

	def insert_post(self, subject, comment, thread_id):
		postgres_insert_query = """ INSERT INTO posts (post_subject, post_comment, thread_id) VALUES (%s,%s,%s) RETURNING id;"""
		record_to_insert = (subject, comment, thread_id)

		self.cursor.execute(postgres_insert_query, record_to_insert)
		self.connection.commit()
		row_id = self.cursor.fetchone()[0]
		print (row_id, "Post inserted successfully.")
		return row_id


