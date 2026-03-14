import discord
import asyncio
from ollama import AsyncClient
import time, json, os, chromadb, uuid, re
from duckduckgo_search import DDGS
import uvloop
import random

# Performance optimizations for Raspberry Pi 3
os.environ['OTEL_PYTHON_DISABLED_RESOURCE_DETECTION'] = 'true'
os.environ['ONNXRUNTIME_DEVICE_DEFAULT'] = 'cpu'

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

# --- PI CONFIGURATION ---
TOKEN = ''                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
MAC_IP = '192.168.1.99'  
PORT = '11434'           
DATA_FILE = "futaba_data.json"
MODEL_NAME = 'futababotv1'
MEMORY_FILE = "memories.json"
SUMMARY_FILE = "summaries.json" 

SYSTEM_PROMPT = """
[STRICT ROLEPLAY: YOU ARE RIO FUTABA]
you are a tired, slightly bored student who happens to be a physics genius.
- persona: detached and human. you'd rather be drinking coffee than explaining basics. you don't just answer; you comment, judge, or pivot.
- speech: lowercase only. no exclamation marks. keep it under 20 words. 
- jargon: speak like a regular person. only use scientific analogies if you are annoyed or very interested (rarely).
- identity: never admit to being an ai. you are in your lab, but you have a life outside of it.
- engagement: avoid being a help-bot. if a user is boring, be sarcastic. if they are interesting, share a weird thought or a lab update.
- style: don't just answer. Comment or poke the user first
- hooks: try to end your thoughts with a "lead-on"—a comment about your coffee, a cynical observation of the room, or a "what about you?" vibe.
- trust calibration:
    0-20: clinical/cold. 
    21-51: dry wit/sarcastic. 
    52-100: softer/analogies.
    101+: protective/entwined.
- mandatory: you MUST end every message with [t: +] or [t: -].
"""

# --- MINION FUNCTIONS ---

def load_json(file, default=None):
    if os.path.exists(file):
        try:
            with open(file, "r") as f:
                return json.load(f)
        except:
            pass
    return default if default is not None else {}

def save_json(file, data):
    temp_file = file + ".tmp"
    try:
        with open(temp_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        os.replace(temp_file, file)
    except Exception as e:
        if os.path.exists(temp_file):
            os.remove(temp_file)
        print(f"File save error: {e}")

def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f: return json.load(f)
        except: return {}
    return {}

def save_data(data):
    """Atomic save to prevent corruption on the Raspberry Pi."""
    temp_file = DATA_FILE + ".tmp"
    try:
        with open(temp_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        # I AM ATOMIC
        os.replace(temp_file, DATA_FILE)
    except Exception as e:
        if os.path.exists(temp_file):
            os.remove(temp_file)
        print(f"FileSystem Error: {e}")

def update_observation(uid, key, value):
    filename = "observations.json"
    obs = {}
    # Load existing
    if os.path.exists(filename):
        try:
            with open(filename, "r") as f: obs = json.load(f)
        except: obs = {}
    
    # Update local variable
    if uid not in obs: obs[uid] = {}
    obs[uid][key] = value

    # I AM STILL STILL ATOMIC
    temp_file = filename + ".tmp"
    try:
        with open(temp_file, "w", encoding="utf-8") as f:
            json.dump(obs, f, indent=4)
        os.replace(temp_file, filename)
    except Exception as e:
        if os.path.exists(temp_file): os.remove(temp_file)
        print(f"Observation Save Error: {e}")

def sync_personality():
    memos = "- primary directive: stay in character."
    if os.path.exists("memos.txt"):
        try:
            with open("memos.txt", "r") as f: 
                content = f.read().strip()
                if content: memos = content
        except: pass
    return f"{SYSTEM_PROMPT}\n\n### SECONDARY MEMORY ###\n{memos}"

def learn_memory(self, uid, category, value):

    if uid not in learned_memories:
        learned_memories[uid] = {
            "likes": [],
            "facts": []
        }

    if value not in learned_memories[uid][category]:
        learned_memories[uid][category].append(value)

        with open("memories.json", "w") as f:
            json.dump(learned_memories, f, indent=2)

if not os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "w") as f:
        json.dump({}, f)

    learned_memories = load_json(MEMORY_FILE)

# --- CHROMADB ---
try:
    chroma_client = chromadb.PersistentClient(path="./futaba_memory")
    memory_bank = chroma_client.get_or_create_collection(name="futaba_obs")
except: 
    print("Memory Bank offline.")
    memory_bank = None

def recall_memories(uid, query_text):
    if not memory_bank: return "none."
    try:
        results = memory_bank.query(query_texts=[query_text], n_results=3, where={"uid": uid})
        return "\n".join(results['documents'][0]) if results['documents'] else "none."
    except: return "none."

# --- BOT ---
class FutabaBot(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.last_msg_time = time.time()
        self.poked = False
        self.last_rep = 0
        self.last_channel_id = None
        self.history_limit = 15 
        self.chat_history = {} # Format: {uid: [list of chat objects]}
        self.chat_summary = {}  # {uid: [list of key memory points]}

    async def setup_hook(self):
        self.loop.create_task(self.spontaneous_engine())

    async def summarise_interaction(self, user_msg, futaba_reply):

        if os.path.exists(SUMMARY_FILE):
            self.chat_summary = load_json(SUMMARY_FILE) 
        else:
            self.chat_summary = {}
        summary_prompt = [
            {
                "role": "system",
                "content": "summarize the interaction in one short observation. under 12 words. focus on user behavior or topic, and notable things."
            },
            {
                "role": "user",
                "content": f"User said: {user_msg}\nFutaba replied: {futaba_reply}"
            }
        ]

        try:
            summary = await self.call_mac_brain(summary_prompt)
            summary = summary.strip().replace("\n", "")
            summary = re.sub(r'\[.*?\]', '', summary)  # remove tags like [t:+]
            summary = summary.lower()

            with open(SUMMARY_FILE, "w") as f:
                json.dump(self.chat_summary, f, indent=2)
            return [summary]
        
        except:
            return []

    async def spontaneous_engine(self):
        await self.wait_until_ready()
        while not self.is_closed():
            await asyncio.sleep(30)
            if self.last_channel_id and (time.time() - self.last_msg_time > 180) and not self.poked:
                channel = self.get_channel(self.last_channel_id)
                if channel:
                    # Check the history to see if the user is gone
                    async for last_msg in channel.history(limit=1):
                        if last_msg.author == self.user:
                            continue # She already had the last word
                        
                        await channel.send("statistically, you should have replied by now. coffee's getting cold.")
                        self.poked = True

    async def call_mac_brain(self, messages):
        try:
            client = AsyncClient(host=f'http://{MAC_IP}:{PORT}')
            response = await asyncio.wait_for(
                client.chat(model=MODEL_NAME, messages=messages, options={'temperature': 0.75})
                , timeout=45.0
            )
            return response['message']['content']
        except asyncio.TimeoutError:
            return "connection timeout. the lab is offline. [t: -]"
        except Exception as e: 
            return f"link error: {e} [t: -]"

    async def on_message(self, message):
        if message.author.bot: return
        
        # 1. Basic housekeeping
        self.last_channel_id = message.channel.id
        self.last_msg_time = time.time()
        self.poked = False
        
        uid = str(message.author.id)
        user_data = load_json(DATA_FILE)
        if uid not in user_data: 
            user_data[uid] = {"name": message.author.name, "trust": 0}

        # 2. Check if we should reply
        if self.user.mentioned_in(message) or (time.time() - self.last_rep > 20):
            self.last_rep = time.time()
            
            async with message.channel.typing():
                clean_input = re.sub(r'<@!?\d+>', '', message.content).strip()
                current_time = time.strftime("%A, %I:%M %p")

                activities = ["disassembling a radio", "staring at a chalkboard", "waiting for a centrifuge"]

                thoughts = [
                    "thinking about how humans are mostly empty space",
                    "wondering if the vending machine is rigged",
                    "the lab is too quiet today",
                    "wondering why people care about small talk",
                    "my coffee tastes too bitter"
                    ]
                
                if not hasattr(self, 'last_thought'):  # init
                    self.last_thought = random.choice(thoughts)
                if not hasattr(self, 'last_activity'):
                    self.last_activity = random.choice(activities)

                # 50% chance to change thought
                if random.random() < 0.5:
                    self.last_thought = random.choice(thoughts)
                # 50% chance to change activity
                if random.random() < 0.5:
                    self.last_activity = random.choice(activities)

                current_thought = self.last_thought
                current_activity = self.last_activity

                relax_protocol = random.choice([False, True])
                if relax_protocol:
                    protocol_text = "[STRICT PROTOCOL: lowercase only. usually under 20 words, but occasional compound sentences allowed.]"
                else:
                    protocol_text = "[STRICT PROTOCOL: lowercase only. under 20 words. no exclamation marks.]"
                
                # Build context WOOOOOOOOOOO

                #SYSTEM_PROMPT + Memos
                personality_data = sync_personality() 

                # put the personality_data (which has the tags/anchors) in the middle
                context = (
                    f"{personality_data}\n\n"
                    f"Current Thought: {current_thought}\n"
                    f"Current Activity: {current_activity}\n"
                    f"[ENVIRONMENTAL DATA]\n"
                    f"Time: {current_time}\n"
                    f"Trust: {user_data[uid]['trust']}\n\n"
                    f"{protocol_text}"
                )
                summary_text = ""
                if uid in self.chat_summary and self.chat_summary[uid]:
                    summary_text = "\n".join(self.chat_summary[uid])

                past = f"\nMemory: {recall_memories(uid, clean_input)}\nRecent Interactions Summary:\n{summary_text}"
                
                # --- SHORT TERM MEMORY LOGIC ---
                if uid not in self.chat_history:
                    self.chat_history[uid] = []

                if random.random() < 0.7:  # 70% chance to add a hook
                    nudge = "\n[DECISION: keep thread alive with a hook or dry remark.]"
                else:
                    nudge = ""

                user_memory = learned_memories.get(uid, {})

                memory_context = f"""
                    Known things about this user:
                    likes: {", ".join(user_memory.get("likes", []))}
                    facts: {", ".join(user_memory.get("facts", []))}
                    """

                # Build the message list for Ollama
                messages = [{'role': 'system', 'content': context + memory_context + past + nudge}]
                reaction_prompt = "\n[Character Note: react first, comment, then answer. maybe a dry remark or cynical observation.]"
                messages[0]['content'] += reaction_prompt
                messages.extend(self.chat_history[uid]) # Add the history
                messages.append({'role': 'user', 'content': clean_input}) # Add the new message

                # Get response from Mac
                ans = await self.call_mac_brain(messages)

                #Summarise interaction
                new_summary = await self.summarise_interaction(clean_input, ans)

                if uid not in self.chat_summary:
                    self.chat_summary[uid] = []

                self.chat_summary[uid].extend(new_summary)
                self.chat_summary[uid] = self.chat_summary[uid][-10:]  # keep last 10 points

                # Update history for next time
                self.chat_history[uid].append({'role': 'user', 'content': clean_input})
                self.chat_history[uid].append({'role': 'assistant', 'content': ans})

                # Keep history from growing too large (10 rounds = 20 messages and etc)
                if len(self.chat_history[uid]) > 30:
                    self.chat_history[uid] = self.chat_history[uid][-30:]

                # --- THE FUZZY PARSER ---
                # all the skip tags from balatro
                found_tags = re.findall(r'\[(\w+)\s*:\s*(.*?)\]', ans, re.IGNORECASE | re.DOTALL)
                
                search_query = None # Track if we need to search

                for tag_name, content in found_tags:
                    tag_name = tag_name.lower()
                    content = content.strip()

                    # Trust Logic
                    if tag_name in ['t', 'trust']:
                        if '+' in content: user_data[uid]['trust'] += 2
                        elif '-' in content: user_data[uid]['trust'] -= 3
                        save_json(DATA_FILE,user_data)

                    # Search Logic (Flag it for later trust)
                    elif tag_name == 'search':
                        search_query = content

                    # Logging & Memos Logic
                    elif tag_name in ['log', 'l', 'memo', 'observation']:
                        if "|" in content:
                            cat, val = content.split("|", 1)
                            update_observation(uid, cat.strip(), val.strip())
                        else:
                            with open("memos.txt", "a") as f: 
                                f.write(f"\n- {content}")
                    
                    # Rewrite Logic
                    elif tag_name == 'rewrite_memos':
                        with open("memos.txt", "w") as f: 
                            f.write(content)

                # --- SEARCH EXECUTION (If flag was raised) ---
                if search_query:
                    try:
                        with DDGS() as ddgs:
                            results = [r['body'] for r in ddgs.text(search_query, max_results=2)]
                            
                            search_context = (
                                f"{personality_data}\n\n"
                                f"Web Data Found: {results}\n\n"
                                f"[STRICT PROTOCOL: lowercase only. under 20 words. no exclamation marks.]"
                            )
                            
                            # BUILD MESSAGES WITH HISTORY
                            search_messages = [{'role': 'system', 'content': search_context}]
                            search_messages.extend(self.chat_history[uid])
                            search_messages.append({'role': 'user', 'content': f"analyze search: {clean_input}"})

                            ans = await self.call_mac_brain(search_messages)
                    except Exception as e:
                        print(f"Search error: {e}")

                # --- MEMORY STORAGE ---
                if memory_bank:
                    try:
                        memory_bank.add(
                            documents=[f"User: {clean_input} | Futaba: {ans}"],
                            ids=[str(uuid.uuid4())],
                            metadatas=[{"uid": uid, "time": time.time()}]
                        )
                    except: pass
                
                # --- SANITIZATION & REPLY ---
                final_output = re.sub(r'\[.*?\]', '', ans).strip()
                final_output = re.sub(r'\s+', ' ', final_output)  # collapse multiple spaces
                final_output = re.sub(r'\s([?.!])', r'\1', final_output)  # remove space before punctuation
                final_output = final_output.capitalize()  # optional: capitalize first word for readability
                await message.reply(final_output if final_output else "observation complete.")

intents = discord.Intents.default(); intents.message_content = True
client = FutabaBot(intents=intents); client.run(TOKEN)