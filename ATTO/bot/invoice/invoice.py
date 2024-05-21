from main import *


async def send_invoice_and_clear(bot, user_id, total_amount, state):
    try:
        product_name = 'ATTO'
        prices = [LabeledPrice(label=product_name, amount=total_amount)]

        await bot.send_invoice(user_id,
                               title="ATTO",
                               description=f"{product_name}  {total_amount}",
                               provider_token=PROVIDER_TOKEN_CLICK,
                               currency="uzs",
                               need_email=True,
                               prices=prices,
                               start_parameter="example",
                               payload="some_invoice")
    except Exception as e:
        await bot.send_message(user_id, f"Xatolik yuz berdi: {e}")
    finally:
        await state.clear()
