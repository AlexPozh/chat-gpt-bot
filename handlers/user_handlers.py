from aiogram import Router, F

from aiogram.types import Message

from aiogram.filters import Command, CommandStart

from lexicon.lexiconENG import LEXICON_ENG

from aiogram.fsm.context import FSMContext

from aiogram.fsm.state import State, StatesGroup, default_state

from aiogram.fsm.storage.memory import MemoryStorage

from external_services.chat_ai import make_promt_gpt_3_5

router = Router()

# init storage for our states
storage: MemoryStorage = MemoryStorage()

# class for FSM context
class ContinueDialogueFSM(StatesGroup):
    # user's answer
    continue_dialogue = State()



@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(
        text=LEXICON_ENG[message.text]
    )


@router.message(F.content_type.in_(['audio', "sticker", "photo", "voice", "video", "animation"]))
async def echo_message(message: Message):
    await message.reply(
        text=LEXICON_ENG["others"]
    )


@router.message(F.content_type.in_(['text']))
async def echo_message(message: Message):
    response = await make_promt_gpt_3_5(message.text)
    await message.answer(
        text=response
    )
