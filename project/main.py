from tiendavirtual import *

def main() -> None:
  app = Application.builder().token("5564690109:AAHStdlo-Pt73uW1aOZMQgJ6xt4oDC41JUU").build()
  
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
