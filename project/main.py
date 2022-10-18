from tiendavirtual import *

def main() -> None:
  persistence = PicklePersistence(filepath="databot")
  app = Application.builder().token("5564690109:AAHStdlo-Pt73uW1aOZMQgJ6xt4oDC41JUU").persistence(persistence).arbitrary_callback_data(True).build()
  
  convHandler = ConversationHandler(
    entry_points = [CommandHandler("start", start)],
    states = {
      BUY : [MessageHandler(filters.Regex("^(t-shirt|pants|shoes|computer|car)$"), buy)]
      },
    fallbacks=[CommandHandler("cancel", cancel)],
  )
  
  app.add_handler(convHandler)
  app.run_polling()

if __name__ == "__main__":
  main()
