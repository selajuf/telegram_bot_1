from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext, filters
from aiogram.dispatcher.filters.state import State, StatesGroup


class FSM(StatesGroup):
    Question_1 = State()
    Question_2 = State()
    Question_3 = State()
    Question_4 = State()
    Question_5 = State()
    Question_6 = State()
    Question_7 = State()
    Question_8 = State()
    Question_9 = State()
    Question_10 = State()
    Question_11 = State()
    Question_12 = State()
    Question_13 = State()
    Question_14 = State()
    Question_15 = State()
    Question_16 = State()
    Question_17 = State()
    Question_18 = State()
    Question_19 = State()
    Question_20 = State()
    Question_21 = State()
    Question_22 = State()
    Question_23 = State()
    Question_24 = State()
    Question_25 = State()
    Question_26 = State()
    Question_27 = State()
    Question_28 = State()
    Question_29 = State()
    Question_30 = State()
    Question_31 = State()
    Question_32 = State()
    Question_33 = State()
    Question_34 = State()


async def Q1(message: types.Message):
    await FSM.Question_1.set()
    await message.answer('Опишите кратко с какой проблемой Вы столкнулись?')


async def Q2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Question_2'] = message.text
    await FSM.next()
    await message.answer('Какой возник корпоративный конфликт ?')


async def Q3(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Question_3'] = message.text
    await FSM.next()
    await message.answer('Когда Вы узнали о нарушении?')


async def Q4(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Question_4'] = message.text
    await FSM.next()
    await message.answer('При каких обстоятельствах Вы узнали?')


async def Q5(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Question_5'] = message.text
    await FSM.next()
    await message.answer('Кем Вы являетесь?')


async def Q6(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Question_6'] = message.text
    await FSM.next()
    await message.answer('Сколько у Вас % голосующих акций?')


async def Q7(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Question_7'] = message.text
    await FSM.next()
    await message.answer('Сколько у Вас % голосов?')


async def Q8(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Question_8'] = message.text
    await FSM.next()
    await message.answer('Вид деятельности организации? (на чем специализируется?)')


async def Q9(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Question_9'] = message.text
    await FSM.next()
    await message.answer('Где находится организация?')


async def Q10(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Question_10'] = message.text
    await FSM.next()
    await message.answer('Какая была заключена сделка?')


async def Q11(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Question_11'] = message.text
    await FSM.next()
    await message.answer('Была ли необходимость в заключении сделки ?')


async def Q12(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Question_12'] = message.text
    await FSM.next()
    await message.answer('Предмет и условия договора?')


async def Q13(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Question_13'] = message.text
    await FSM.next()
    await message.answer('Сумма сделки?')


async def Q14(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Question_14'] = message.text
    await FSM.next()
    await message.answer('Является ли сумма ниже рыночной?')


async def Q15(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Question_15'] = message.text
    await FSM.next()
    await message.answer(
        '-Есть ли у вас документы, подтверждающие данный факт (проводилась ли Вами оценочная экспертиза)?')


async def Q16(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Question_16'] = message.text
    await FSM.next()
    await message.answer('Кто контрагент?')


async def Q17(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Question_17'] = message.text
    await FSM.next()
    await message.answer('В чем проявляется заинтересованность?')


async def Q18(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Question_18'] = message.text
    await FSM.next()
    await message.answer('Было ли исполнение по данному договору?')


async def Q19(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Question_19'] = message.text
    await FSM.next()
    await message.answer('Был ли соблюден порядок одобрения сделки?')


async def Q20(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Question_20'] = message.text
    await FSM.next()
    await message.answer('Директором была раскрыта информация о конфликте интересов?')


async def Q21(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Question_21'] = message.text
    await FSM.next()
    await message.answer('Была ли одобрена сделка?')


async def Q22(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Question_22'] = message.text
    await FSM.next()
    await message.answer('Директор совершил сделку без одобрения органов юридического лица?')


async def Q23(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Question_23'] = message.text
    await FSM.next()
    await message.answer('Была ли предоставлена информация в отношении такой сделки?')


async def Q24(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Question_24'] = message.text
    await FSM.next()
    await message.answer('Директор как-то пытался сокрыть информацию о сделке?')


async def Q25(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Question_25'] = message.text
    await FSM.next()
    await message.answer('Директором была предоставлена недостоверная информация?')


async def Q26(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Question_26'] = message.text
    await FSM.next()
    await message.answer('Директор предоставил документы после своего увольнения?')


async def Q27(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Question_27'] = message.text
    await FSM.next()
    await message.answer('Имеется ли копия ответа по запросу?')


async def Q28(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Question_28'] = message.text
    await FSM.next()
    await message.answer('В чем заключается ущерб от сделки?')


async def Q29(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Question_29'] = message.text
    await FSM.next()
    await message.answer('Повлекло ли налоговые последствия? Имеются ли у вас копия решения ФНС')


async def Q30(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Question_30'] = message.text
    await FSM.next()
    await message.answer('Повлекло ли вывод активов из фирмы??')


async def Q31(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Question_31'] = message.text
    await FSM.next()
    await message.answer('Привело ли к существенным изменениям масштабов?')


async def Q32(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Question_32'] = message.text
    await FSM.next()
    await message.answer('Имеются ли у Вас материалы, подтверждающие ущерб от такой сделки?')


async def Q33(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Question_33'] = message.text
    await FSM.next()
    await message.answer('Имеет ли место в корпорации длительный внутрикорпоративный конфликт?')


async def Q34(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Question_34'] = message.text
    async with state.proxy() as data:
        await message.answer(str(data))
    await state.finish()


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(Q1, commands='start', state=None)
    dp.register_message_handler(Q2, state=FSM.Question_1)
    dp.register_message_handler(Q3, state=FSM.Question_2)
    dp.register_message_handler(Q4, state=FSM.Question_3)
    dp.register_message_handler(Q5, state=FSM.Question_4)
    dp.register_message_handler(Q6, state=FSM.Question_5)
    dp.register_message_handler(Q7, state=FSM.Question_6)
    dp.register_message_handler(Q8, state=FSM.Question_7)
    dp.register_message_handler(Q9, state=FSM.Question_8)
    dp.register_message_handler(Q10, state=FSM.Question_9)
    dp.register_message_handler(Q11, state=FSM.Question_10)
    dp.register_message_handler(Q12, state=FSM.Question_11)
    dp.register_message_handler(Q13, state=FSM.Question_12)
    dp.register_message_handler(Q14, state=FSM.Question_13)
    dp.register_message_handler(Q15, state=FSM.Question_14)
    dp.register_message_handler(Q16, state=FSM.Question_15)
    dp.register_message_handler(Q17, state=FSM.Question_16)
    dp.register_message_handler(Q18, state=FSM.Question_17)
    dp.register_message_handler(Q19, state=FSM.Question_18)
    dp.register_message_handler(Q20, state=FSM.Question_19)
    dp.register_message_handler(Q21, state=FSM.Question_20)
    dp.register_message_handler(Q22, state=FSM.Question_21)
    dp.register_message_handler(Q23, state=FSM.Question_22)
    dp.register_message_handler(Q24, state=FSM.Question_23)
    dp.register_message_handler(Q25, state=FSM.Question_24)
    dp.register_message_handler(Q26, state=FSM.Question_25)
    dp.register_message_handler(Q27, state=FSM.Question_26)
    dp.register_message_handler(Q28, state=FSM.Question_27)
    dp.register_message_handler(Q29, state=FSM.Question_28)
    dp.register_message_handler(Q30, state=FSM.Question_29)
    dp.register_message_handler(Q31, state=FSM.Question_30)
    dp.register_message_handler(Q32, state=FSM.Question_31)
    dp.register_message_handler(Q33, state=FSM.Question_32)
    dp.register_message_handler(Q34, state=FSM.Question_33)
