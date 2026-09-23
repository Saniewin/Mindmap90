import React, { useState, useEffect } from 'react';
import { ChevronRight, ChevronLeft, Info, Heart, Activity, Brain, BookOpen, X, Moon, Utensils, Star, Shield, Users, Lightbulb, MonitorPlay } from 'lucide-react';

const monthData = [
  {
    month: 1,
    title: "The Newborn Phase",
    description: "A time of feeding, sleeping, and growth. Interactions are mostly reflexive, but your baby is already learning your voice and smell.",
    milestones: [
      { category: "Motor", text: "Exhibits early reflexes: Rooting (turns head to touch), Moro (startle reflex), and grasping." },
      { category: "Sensory", text: "Focuses on objects 8-12 inches away (perfect distance to your face). Prefers sweet tastes." },
      { category: "Social/Emotional", text: "Level 1: Shared Attention and Regulation begins. The infant seeks to establish calm alertness and basic rhythms." }
    ],
    parenting: {
      feeding: "Breast or bottle feed 2–3 to 4–5 hourly on demand. Aim for ~30g weight gain per day.",
      sleep: "Aim for 18–21 hours of sleep per day. Life is essentially feed, sleep, feed, sleep.",
      activities: "Begin 'Serve and Return' by making eye contact and using a high-pitched, gentle voice."
    },
    guides: [
      { id: 'serve-return', title: "How-To: Serve and Return", icon: <Activity size={18}/> },
      { id: 'mother-care', title: "Learn More: Postpartum Nutrition", icon: <Heart size={18}/> }
    ]
  },
  {
    month: 2,
    title: "The Month of Awakening",
    description: "The baby is learning about affection and will put energy into increasing parent contact time. Smiling commences.",
    milestones: [
      { category: "Motor", text: "Able to raise chin from ground and turn head from side-to-side." },
      { category: "Language", text: "Begins to produce simple 'cooing' sounds consisting mainly of vowels." },
      { category: "Social/Emotional", text: "Develops the first social smile—a delightful and unforgettable moment!" }
    ],
    parenting: {
      feeding: "Continue feeding on demand. Baby's hunger signals may become more recognizable.",
      sleep: "18-21 hours of sleep is still normal. Start guiding the baby to sleep independently.",
      activities: "Introduce tummy time for a few minutes a day to strengthen neck and shoulder muscles."
    },
    guides: [
      { id: 'tummy-time', title: "How-To: Tummy Time Basics", icon: <Activity size={18}/> },
      { id: 'crying-cues', title: "Learn More: Understanding Cries", icon: <Info size={18}/> }
    ]
  },
  {
    month: 3,
    title: "Establishing Patterns",
    description: "The baby is developing significant social skills, obvious interest in the family, and predictable routines.",
    milestones: [
      { category: "Motor", text: "Can play with hands and fingers, and brings objects in hand to mouth." },
      { category: "Cognitive", text: "Starts to anticipate eating at the sight of food or a bottle." },
      { category: "Social/Emotional", text: "Vocalizes to express pleasure. Level 2: Engagement and Relating." }
    ],
    parenting: {
      feeding: "Feeding patterns become more predictable around the 24-hour clock.",
      sleep: "Evening bedtime begins to develop predictability (6-7 PM). Aim to achieve 12 hours at night (with 1-2 feeds).",
      activities: "Read simple, high-contrast board books. Sing nursery rhymes to encourage auditory tracking."
    },
    guides: [
      { id: 'sleep-training', title: "How-To: Bedtime Routines", icon: <Moon size={18}/> },
      { id: 'psych-dev', title: "Learn More: Early Psychological Milestones", icon: <Brain size={18}/> }
    ]
  },
  {
    month: 4,
    title: "The Explorer Emerges",
    description: "Physical strength increases dramatically. Your baby is becoming a much more active participant in the family.",
    milestones: [
      { category: "Motor", text: "Rolls from abdomen to back. Sits propped up for 10 to 15 minutes." },
      { category: "Language", text: "Gets excited, laughs aloud. Babbling begins, repeating simple consonant and vowel sounds." },
      { category: "Sensory", text: "Vision improves; can track moving objects across the room smoothly." }
    ],
    parenting: {
      feeding: "First teeth may begin to appear soon. Prepare safe teething toys.",
      sleep: "Sleep regressions may occur as brain development leaps forward. Stick to routines.",
      activities: "Provide colorful play mats. Encourage reaching and grasping by dangling safe toys."
    },
    guides: [
      { id: 'teething', title: "How-To: Soothe a Teething Baby", icon: <Star size={18}/> },
      { id: 'milestone-tracking', title: "Learn More: Tracking Gross Motor", icon: <Info size={18}/> }
    ]
  },
  {
    month: 5,
    title: "Reaching Out",
    description: "Your baby's world is expanding as they learn to use their hands to explore and their voice to demand attention.",
    milestones: [
      { category: "Motor", text: "Sits on lap, reaches, and grasps objects purposefully." },
      { category: "Cognitive", text: "Begins to understand cause and effect (e.g., shaking a rattle makes a sound)." },
      { category: "Social/Emotional", text: "Smiles spontaneously in response to people. Shows strong attachment to primary caregivers." }
    ],
    parenting: {
      feeding: "Continue milk feeds. Talk to your pediatrician about readiness for solid foods.",
      sleep: "Naps may consolidate into 2-3 longer periods during the day.",
      activities: "Play 'peek-a-boo' to start teaching object permanence. Talk through your daily chores."
    },
    guides: [
      { id: 'peek-a-boo', title: "How-To: Games for Brain Growth", icon: <Brain size={18}/> }
    ]
  },
  {
    month: 6,
    title: "The Half-Year Mark",
    description: "A major transition month featuring the introduction of solid foods and independent sitting.",
    milestones: [
      { category: "Motor", text: "Sits alone unsupported for brief periods. Stands with help." },
      { category: "Cognitive", text: "Smiles and vocalizes to a mirror, patting at their mirror image." },
      { category: "Feeding", text: "Exhibits tongue lateralization (side-to-side movement) necessary for swallowing solids." }
    ],
    parenting: {
      feeding: "Starts accepting baby food (purées or baby-led weaning). Watch for tongue thrust expulsion.",
      sleep: "Many babies sleep through the night (6-8 hours without waking), though variations are normal.",
      activities: "Introduce a sippy cup with a small amount of water. Give them safe household objects (wooden spoons) to explore."
    },
    guides: [
      { id: 'solids', title: "How-To: Introducing Solid Foods", icon: <Utensils size={18}/> },
      { id: 'psych-dev', title: "Learn More: Early Psychological Milestones", icon: <Brain size={18}/> }
    ]
  },
  {
    month: 7,
    title: "On the Move",
    description: "Coordination is rapidly improving. Your baby is likely figuring out how to mobilize.",
    milestones: [
      { category: "Motor", text: "Transfers objects from hand to hand. May begin crawling or scooting." },
      { category: "Language", text: "Responds to their own name and recognizes the word 'no'." },
      { category: "Social/Emotional", text: "Level 3: Two-Way Purposeful Emotional Interactions. Initiates and responds to signals." }
    ],
    parenting: {
      feeding: "Offer a variety of pureed flavors and textures. Introduce common allergens carefully.",
      sleep: "Separation anxiety may disrupt sleep. Offer quiet reassurance without turning on lights.",
      activities: "Child-proof the house! Get down on their level to see potential hazards."
    },
    guides: [
      { id: 'baby-proofing', title: "How-To: Essential Baby-Proofing", icon: <Info size={18}/> }
    ]
  },
  {
    month: 8,
    title: "Crawling and Creeping",
    description: "Exploration is the name of the game. They are actively investigating their environment.",
    milestones: [
      { category: "Motor", text: "Sits alone without support indefinitely. Begins crawling and creeping." },
      { category: "Cognitive", text: "Object permanence is established; they will look for a hidden toy." },
      { category: "Social/Emotional", text: "Stranger anxiety may peak as they clearly differentiate familiar faces from unfamiliar ones." }
    ],
    parenting: {
      feeding: "Pincer grasp is developing; offer safe, soft finger foods (e.g., ripe banana, avocado).",
      sleep: "Maintain consistent nap and bedtime routines to provide security during developmental leaps.",
      activities: "Hide toys under blankets and encourage them to find them. Practice pointing at objects."
    },
    guides: [
      { id: 'stranger-anxiety', title: "Learn More: Managing Stranger Anxiety", icon: <Heart size={18}/> }
    ]
  },
  {
    month: 9,
    title: "Pulling Up",
    description: "Legs are getting stronger, and vertical exploration begins. Gestural communication improves.",
    milestones: [
      { category: "Motor", text: "Pulls self to standing by holding onto furniture." },
      { category: "Language", text: "Narrows babbling to sounds of their native language. Uses pointing to communicate." },
      { category: "Cognitive", text: "Teleological thinking emerges: observing physical reality to infer goal-directed actions." }
    ],
    parenting: {
      feeding: "Takes solids well. Continue offering family foods mashed to safe consistencies.",
      sleep: "Ensure the crib mattress is lowered to the bottom setting now that they can stand.",
      activities: "Place toys on low tables to encourage pulling up. Read interactive flap books."
    },
    guides: [
      { id: 'gestures', title: "How-To: Encouraging Pointing and Gestures", icon: <Activity size={18}/> }
    ]
  },
  {
    month: 10,
    title: "Standing Alone",
    description: "Balancing acts begin. Your baby is mastering the transition between sitting, standing, and crawling.",
    milestones: [
      { category: "Motor", text: "Stands alone momentarily. Walks with help (cruising)." },
      { category: "Language", text: "May say 'mamma' or 'dada' specifically to the correct parent." },
      { category: "Social/Emotional", text: "Social referencing: Seeks out your emotional reaction to gauge their own (e.g., looking at you when they fall)." }
    ],
    parenting: {
      feeding: "Encourage self-feeding with a spoon, even if it's messy. It builds fine motor skills.",
      sleep: "May drop to a single long nap during the day, though two is still common.",
      activities: "Provide sturdy push-toys to help them practice walking safely."
    },
    guides: [
      { id: 'social-referencing', title: "Learn More: Social Referencing", icon: <Brain size={18}/> }
    ]
  },
  {
    month: 11,
    title: "The Communicator",
    description: "Receptive language is booming. They understand much more than they can say.",
    milestones: [
      { category: "Motor", text: "Stands well alone. When held standing, supports most of own weight." },
      { category: "Language", text: "Gives a toy in response to a request or gesture. Follows simple commands." },
      { category: "Cognitive", text: "Cooperates when being dressed (e.g., holding out an arm for a sleeve)." }
    ],
    parenting: {
      feeding: "Moving towards 3 meals and 2 snacks a day. Breastmilk or formula is still a primary nutrient source.",
      sleep: "Consistency is key as they test boundaries. Hold firm to established sleep habits.",
      activities: "Give them simple tasks ('bring me the ball'). Listen to and validate their babbling conversations."
    },
    guides: [
      { id: 'receptive-language', title: "How-To: Boost Receptive Language", icon: <BookOpen size={18}/> }
    ]
  },
  {
    month: 12,
    title: "The First Birthday",
    description: "Congratulations! You have a toddler. This month is marked by independent steps and first true words.",
    milestones: [
      { category: "Motor", text: "Walks with only one hand held, or takes first steps alone." },
      { category: "Language", text: "Says 'mamma' and 'dada' and perhaps two other words purposefully." },
      { category: "Social/Emotional", text: "Plays 'peek-a-boo' and other social games with anticipation and joy." }
    ],
    parenting: {
      feeding: "Can transition to whole cow's milk (if advised by pediatrician). Eats mostly mashed table food.",
      sleep: "Needs 11-14 hours of sleep in a 24-hour period.",
      activities: "Celebrate! Continue narrative play, stacking blocks, and rolling balls back and forth."
    },
    guides: [
      { id: 'first-steps', title: "Learn More: Supporting First Steps", icon: <Activity size={18}/> },
      { id: 'psych-dev', title: "Learn More: Early Psychological Milestones", icon: <Brain size={18}/> }
    ]
  },
  {
    month: 15,
    title: "The Walker & Explorer",
    description: "Your toddler is likely walking independently and exploring everything. Receptive language is growing rapidly, meaning they understand much more than they can say.",
    milestones: [
      { category: "Motor", text: "Walks well, creeps up stairs, and can stack two blocks or scribble spontaneously." },
      { category: "Language", text: "Uses 3-5 words correctly, points to objects to ask for them or show them to you." },
      { category: "Cognitive", text: "Understands simple commands like 'give it to me' and follows a 1-step direction." }
    ],
    parenting: {
      feeding: "Transition fully to a cup and offer a variety of safe, soft finger foods. Picky eating may begin to surface.",
      sleep: "May transition from two naps down to one afternoon nap. Total sleep should be around 11-14 hours.",
      activities: "Provide shape sorters and stacking rings. Read board books and let them turn the pages."
    },
    guides: [
      { id: 'setting-limits', title: "How-To: Setting Positive Limits", icon: <Shield size={18}/> }
    ]
  },
  {
    month: 18,
    title: "The Emerging Talker",
    description: "Vocabulary is expanding, and your toddler is increasingly asserting their independence. This is the stage of 'No!' and 'Mine!', accompanied by big emotions.",
    milestones: [
      { category: "Motor", text: "Runs stiffly, walks up steps holding a hand, and can use a spoon with some spilling." },
      { category: "Language", text: "Has a vocabulary of about 10-20 words. Looks at pictures in a book." },
      { category: "Social/Emotional", text: "Rapprochement Phase: Explores independently but frequently returns to you for emotional 'refueling'." }
    ],
    parenting: {
      feeding: "Appetite may decrease as growth slows. Offer healthy choices but let them decide how much to eat.",
      sleep: "Usually firmly on a one-nap schedule. Bedtime boundaries and routines may be tested.",
      activities: "Provide pots and pans for drum play, or dolls for early pretend play. Use simple matching games."
    },
    guides: [
      { id: 'temper-tantrums', title: "Learn More: Managing Tantrums", icon: <Heart size={18}/> },
      { id: 'rapprochement', title: "Learn More: The Rapprochement Phase", icon: <Brain size={18}/> }
    ]
  },
  {
    month: 24,
    title: "Two Years Old!",
    description: "Your two-year-old is a curious, active, and highly expressive person making massive cognitive leaps, particularly in symbolic play and communication.",
    milestones: [
      { category: "Motor", text: "Walks up and down stairs alone, runs well without falling, and kicks a ball." },
      { category: "Language", text: "Speaks in 2-3 word sentences ('me go', 'want juice'), uses personal pronouns ('I' and 'you')." },
      { category: "Social/Emotional", text: "Parallel play is dominant. Begins to show self-conscious emotions like shame, guilt, and pride." }
    ],
    parenting: {
      feeding: "Include them in family meals. Teach them to wipe the table to build competence and confidence.",
      sleep: "May show signs of toilet training readiness (staying dry for 2+ hours, showing interest in the bathroom).",
      activities: "Play 'Follow the Leader', sort colors and shapes, and build block towers."
    },
    guides: [
      { id: 'parallel-play', title: "Learn More: Understanding Parallel Play", icon: <Users size={18}/> },
      { id: 'potty-training', title: "How-To: Toilet Training Readiness", icon: <Info size={18}/> }
    ]
  },
  {
    month: 30,
    title: "The Imaginative Thinker",
    description: "Imagination is blossoming. Your toddler is beginning to understand others' feelings and can follow routine multi-step directions.",
    milestones: [
      { category: "Motor", text: "Jumps with both feet, has good hand-finger coordination for scribbling or simple puzzles." },
      { category: "Cognitive", text: "Answers simple questions, identifies themselves by name, stays with activities for 3+ minutes." },
      { category: "Social/Emotional", text: "Beginning to understand the concept of sharing (but rarely wants to), getting louder and bossier at times." }
    ],
    parenting: {
      feeding: "Foster independence by letting them use an open cup and serve themselves simple foods.",
      sleep: "Nightmares or fears of the dark may begin due to their rapidly developing imagination.",
      activities: "Provide dress-up clothes for dramatic play, finger paint, and sing interactive nursery rhymes."
    },
    guides: [
      { id: 'giving-choices', title: "How-To: The Power of Choices", icon: <Lightbulb size={18}/> },
      { id: 'night-fears', title: "Learn More: Handling Nighttime Fears", icon: <Moon size={18}/> }
    ]
  },
  {
    month: 36,
    title: "The Preschooler",
    description: "Congratulations, you have a preschooler! This year brings rich fantasy play, the ability to take turns, and a deep desire to help.",
    milestones: [
      { category: "Motor", text: "Alternates feet when climbing stairs, rides a tricycle, and can copy a circle." },
      { category: "Language", text: "Speaks in full sentences, comprehends and answers questions. Knows and repeats simple rhymes." },
      { category: "Social/Emotional", text: "Plays cooperatively with others, shows concern for a crying friend, understands simple rules." }
    ],
    parenting: {
      feeding: "Feeds self with little spilling. Can help with simple, safe cooking tasks like stirring or pouring.",
      sleep: "May resist bedtime to keep playing. Maintain a predictable, calming 30-minute wind-down routine.",
      activities: "Team up for household chores, encourage active outdoor play, and arrange playdates."
    },
    guides: [
      { id: 'power-of-play', title: "Learn More: The Power of Play", icon: <Activity size={18}/> },
      { id: 'empathy-building', title: "How-To: Building Early Empathy", icon: <Heart size={18}/> }
    ]
  }
];

const guideContent = {
  'serve-return': {
    title: "Serve and Return: Brain Building",
    content: "Think of your baby's brain development like a game of tennis. When they 'serve' by cooing, pointing, or looking at you, 'return' the ball by making eye contact, smiling, or speaking back. This back-and-forth interaction is the foundation of emotional and cognitive development. It tells the baby they are understood and helps wire vital neural connections."
  },
  'mother-care': {
    title: "Postpartum Nutrition & Care",
    content: "While breastfeeding, maternal physiology changes significantly. Energy needs increase by a factor of 50-100%. Aim to increase caloric intake by at least 2,000 calories per day (total) and drink 1-1.5 Liters of milk or hydrating fluids. Caring for the mother's physical and emotional well-being is a fundamental part of caring for the child."
  },
  'tummy-time': {
    title: "Tummy Time Basics",
    content: "Tummy time is crucial for developing the neck, shoulder, and core strength needed for rolling, crawling, and eventually walking. Start with 3-5 minutes, 2-3 times a day while the baby is awake and alert. Get down on their level, use mirrors or high-contrast toys to keep them engaged. Never leave a baby unattended during tummy time."
  },
  'crying-cues': {
    title: "Understanding Cries & Mutual Regulation",
    content: "In the first months, crying is the baby's primary communication. A prompt and consistent response to crying is associated with a decrease in the frequency of crying in subsequent months. Through mutual regulation, the infant uses the caregiver's physical and emotional state to organize their own nervous system. A calm caregiver helps create a calm baby."
  },
  'sleep-training': {
    title: "Establishing Bedtime Routines",
    content: "Sleep is a learned skill. By 3 months, you can establish a predictable pattern. Keep the environment dark and quiet at night. Use parent-independent cues for sleep (like a specific lullaby, a sleep sack, or a white noise machine). Recognize signs of fatigue early—if a child becomes overtired, their ability to settle and sleep is impaired."
  },
  'psych-dev': {
    title: "Psychological Milestones & Emotional Capacities",
    content: "According to the literature on CLINICAL PSYCHOLOGY, the first year is critical for psychic reorganization. \n\nAround 6 months, infants enter the 'differentiation phase' (Mahler), moving from self-orientation to social orientation. They begin to understand cause and effect and that actions have goals. \n\nBy 9 months, we see 'Level 3: Two-Way Purposeful Emotional Interactions' emerge, where the baby uses intentional gestures (pointing, facial expressions) to open and close circles of communication. \n\nSocial referencing also begins; the infant seeks out the caregiver's emotional reactions to gauge their own affective reactions to new stimuli."
  },
  'teething': {
    title: "Soothing a Teething Baby",
    content: "First teeth typically appear between 5 and 9 months. Provide safe, chilled (not frozen) teething rings. Gentle gum massages with a clean finger can help. Drooling will increase, so keep the chin dry to prevent rashes. If the baby is in significant distress, consult your pediatrician about appropriate pain relief."
  },
  'milestone-tracking': {
    title: "Tracking Gross Motor Skills",
    content: "Remember that developmental milestones have an average range and a normal range. While early training can accelerate some basic motor skills, it doesn't necessarily make the child athletically superior later. Let your child develop at their own pace, providing a safe environment for them to practice rolling, sitting, and reaching."
  },
  'peek-a-boo': {
    title: "Games for Brain Growth",
    content: "Games like Peek-a-Boo teach 'Object Permanence'—the understanding that objects (and parents) continue to exist even when they cannot be seen. This cognitive milestone helps ease separation anxiety later on. Similarly, handing objects back and forth teaches reciprocity and early social rules."
  },
  'solids': {
    title: "Introducing Solid Foods",
    content: "Around 6 months, infants develop tongue lateralization (side-to-side movement) necessary to move solid food to the back of the mouth. Start with single-ingredient purées or soft, easily mashable foods. Introduce one new food every few days to monitor for allergic reactions. Remember, breastmilk or formula is still the main source of nutrition."
  },
  'baby-proofing': {
    title: "Essential Baby-Proofing",
    content: "As mobility increases, danger increases. Cover electrical outlets, install baby gates at the top and bottom of stairs, secure heavy furniture (bookshelves, dressers) to the wall, and move toxic cleaning supplies to high, locked cabinets. Get on your hands and knees to see the world from their vantage point and identify choking hazards."
  },
  'stranger-anxiety': {
    title: "Managing Stranger Anxiety",
    content: "Stranger anxiety is a healthy, normal sign of cognitive development. It means the baby can distinguish between familiar and unfamiliar faces. To manage it, introduce new people slowly. Have the stranger approach calmly while you are holding the baby. Validate the baby's feelings and provide comfort rather than forcing interaction."
  },
  'gestures': {
    title: "Encouraging Pointing and Gestures",
    content: "Before they can speak, babies communicate via gestures. Pointing is a massive cognitive leap. Encourage it by pointing to objects yourself and naming them. When your baby points to something, acknowledge it: 'Yes, that is a dog!' This validates their communication and bridges the gap to spoken language."
  },
  'social-referencing': {
    title: "Social Referencing",
    content: "When a baby encounters something new (like a loud toy or a friendly dog), they will look to your face before reacting. If you look scared, they will cry. If you smile and speak calmly, they will approach with confidence. Your emotional response serves as their guide to navigating the world safely."
  },
  'receptive-language': {
    title: "Boosting Receptive Language",
    content: "Receptive language (what they understand) develops much faster than expressive language (what they say). Boost it by narrating your day, giving simple one-step directions ('Please give me the block'), and reading books daily. Ask them 'Where is the...' and let them point to the object or picture."
  },
  'first-steps': {
    title: "Supporting First Steps",
    content: "Walking unassisted usually occurs between 12 and 18 months. Create a safe environment with sturdy furniture they can 'cruise' along. Barefoot is best for learning to walk indoors as it helps the foot develop naturally and provides sensory feedback. Praise their efforts, and don't panic when they inevitably fall on their padded bottoms!"
  },
  'setting-limits': {
    title: "Setting Positive Limits",
    content: "As mobility and curiosity increase, so does the need for boundaries. Toddlers are naturally driven to explore, which means they will touch things they shouldn't. Use redirection rather than punishment. Ensure your home is thoroughly baby-proofed so you don't have to constantly say 'no'. When stopping an unsafe behavior, use a firm, calm voice and offer an acceptable alternative."
  },
  'temper-tantrums': {
    title: "Managing Temper Tantrums",
    content: "Tantrums are a normal part of toddlerhood, often stemming from a gap between what they want to do and what their language or motor skills allow them to do. During a tantrum, stay calm. Use a 'Time-in' approach—sit near them and offer a comforting presence. Once they are calm, help them label their feelings: 'You were so mad because we had to leave the park.'"
  },
  'rapprochement': {
    title: "The Rapprochement Phase (16-24 Months)",
    content: "Identified by developmental psychologist Margaret Mahler, 'Rapprochement' is a phase where your toddler becomes acutely aware of their physical separateness from you. This can trigger a resurgence of separation anxiety. You will see them dart away to explore, then quickly run back to you for emotional 'refueling' (a hug or a check-in) before venturing out again. Be a steady, welcoming home base."
  },
  'parallel-play': {
    title: "Understanding Parallel Play",
    content: "Around age two, children engage heavily in 'Parallel Play.' They will play next to other children, often using similar toys, but they won't directly interact or collaborate. This is a crucial stepping stone to cooperative play. Don't force them to share at this stage; they don't yet understand the concept of ownership versus temporary borrowing. Instead, provide multiples of popular toys."
  },
  'potty-training': {
    title: "Toilet Training Readiness",
    content: "Most children show signs of readiness between 24 and 30 months. Look for these cues: staying dry for at least two hours, waking up dry from a nap, showing discomfort with a soiled diaper, hiding to poop, or expressing interest in the toilet. Avoid rushing the process; waiting until the child is physically and emotionally ready makes toilet training much faster and less stressful."
  },
  'giving-choices': {
    title: "The Power of Choices",
    content: "Toddlers crave autonomy. You can reduce power struggles by offering limited, acceptable choices. Instead of asking, 'Do you want to get dressed?' (which invites a 'No!'), ask, 'Do you want to wear the red shirt or the blue shirt?' Both choices lead to the goal of getting dressed, but the child feels empowered and in control of their environment."
  },
  'night-fears': {
    title: "Handling Nighttime Fears",
    content: "As your toddler's cognitive abilities and imagination grow, so does their capacity for fear. Shadows, noises, or dreams can become 'monsters'. Never dismiss their fear as silly. Validate it: 'I see you are scared.' Use a nightlight, leave the door slightly cracked, and consider a 'monster spray' (water in a spray bottle) to give them a sense of control over their environment."
  },
  'power-of-play': {
    title: "The Power of Play & Recess",
    content: "Play is the work of childhood. Rough-and-tumble play, outdoor exploration, and imaginative scenarios are vital. Play allows children to take risks in a safe environment, learn negotiation skills, and process complex emotions. According to the AAP, active outdoor play promotes sensory integration and foundational motor skills essential for lifelong health."
  },
  'empathy-building': {
    title: "Building Early Empathy",
    content: "At three years old, children are beginning to understand that others have feelings different from their own. Foster this by narrating emotions in daily life and in books: 'Look at the puppy's face, he looks sad.' If your child hurts a playmate, instead of just forcing an apology, draw their attention to the consequence: 'Look, Tommy is crying. It hurt when you pushed him. How can we help him feel better?'"
  }
};

export default function App() {
  const [currentMonth, setCurrentMonth] = useState(1);
  const [activeModal, setActiveModal] = useState(null);
  
  const availableMonths = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 18, 24, 30, 36];

  // Auto-scroll to top when month changes
  useEffect(() => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }, [currentMonth]);

  const activeData = monthData.find(m => m.month === currentMonth);

  const openModal = (id) => setActiveModal(id);
  const closeModal = () => setActiveModal(null);

  const nextMonth = () => {
    const currentIndex = availableMonths.indexOf(currentMonth);
    if (currentIndex < availableMonths.length - 1) {
      setCurrentMonth(availableMonths[currentIndex + 1]);
    }
  };

  const prevMonth = () => {
    const currentIndex = availableMonths.indexOf(currentMonth);
    if (currentIndex > 0) {
      setCurrentMonth(availableMonths[currentIndex - 1]);
    }
  };

  return (
    <div className="min-h-screen bg-slate-50 font-sans text-slate-800">
      
      {/* Header */}
      <header className="bg-white shadow-sm sticky top-0 z-10">
        <div className="max-w-4xl mx-auto px-4 py-4 flex flex-col md:flex-row justify-between items-center gap-4">
          <div className="flex items-center gap-3">
            <div className="bg-teal-100 p-2 rounded-full text-teal-600">
              <Star size={24} fill="currentColor" />
            </div>
            <div>
              <h1 className="text-2xl font-bold text-slate-800 leading-tight">Baby & Toddler Steps Guide</h1>
              <p className="text-xs text-slate-500 font-medium">Years 1-3 Progress & Parenting</p>
            </div>
          </div>
          
          {/* Month Navigation */}
          <div className="flex items-center gap-2 bg-slate-100 rounded-full p-1 border border-slate-200">
            <button 
              onClick={prevMonth}
              disabled={currentMonth === 1}
              className={`p-2 rounded-full transition-colors ${currentMonth === 1 ? 'text-slate-300' : 'text-slate-600 hover:bg-white hover:shadow-sm'}`}
            >
              <ChevronLeft size={20} />
            </button>
            <div className="w-40 text-center font-semibold text-teal-700">
              Month {currentMonth} {currentMonth >= 24 ? `(${currentMonth / 12} Yrs)` : currentMonth > 12 ? '(Toddler)' : ''}
            </div>
            <button 
              onClick={nextMonth}
              disabled={currentMonth === 36}
              className={`p-2 rounded-full transition-colors ${currentMonth === 36 ? 'text-slate-300' : 'text-slate-600 hover:bg-white hover:shadow-sm'}`}
            >
              <ChevronRight size={20} />
            </button>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-4xl mx-auto px-4 py-8 pb-24">
        
        {/* Intro Section */}
        <div className="bg-gradient-to-br from-teal-500 to-emerald-600 rounded-3xl p-8 text-white shadow-lg mb-8 transform transition-all duration-500">
          <div className="inline-block bg-white/20 backdrop-blur-sm rounded-full px-4 py-1 text-sm font-semibold mb-4 tracking-wide border border-white/30">
            Month {activeData.month}
          </div>
          <h2 className="text-4xl font-extrabold mb-3">{activeData.title}</h2>
          <p className="text-teal-50 text-lg leading-relaxed max-w-2xl">{activeData.description}</p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          
          {}
          <div className="md:col-span-2 space-y-6">
            <h3 className="text-2xl font-bold text-slate-800 flex items-center gap-2 border-b pb-2">
              <Activity className="text-teal-500" />
              Developmental Milestones
            </h3>
            
            <div className="grid gap-4">
              {activeData.milestones.map((milestone, idx) => (
                <div key={idx} className="bg-white p-5 rounded-2xl shadow-sm border border-slate-100 hover:shadow-md transition-shadow flex items-start gap-4">
                  <div className="bg-teal-50 p-3 rounded-xl text-teal-600 shrink-0">
                    {milestone.category === "Motor" ? <Activity size={20}/> : 
                     milestone.category === "Language" ? <BookOpen size={20}/> : 
                     milestone.category === "Cognitive" ? <Brain size={20}/> : 
                     milestone.category === "Sensory" ? <Star size={20}/> :
                     <Heart size={20}/>}
                  </div>
                  <div>
                    <h4 className="font-bold text-slate-700 text-sm uppercase tracking-wider mb-1">{milestone.category}</h4>
                    <p className="text-slate-600 leading-relaxed">{milestone.text}</p>
                  </div>
                </div>
              ))}
            </div>

            {/* Quick action buttons linking to Modals */}
            {activeData.guides.length > 0 && (
              <div className="pt-6">
                 <h4 className="text-sm font-bold text-slate-400 uppercase tracking-wider mb-4">Deep Dives & Guides</h4>
                 <div className="flex flex-wrap gap-3">
                   {activeData.guides.map(guide => (
                     <button 
                       key={guide.id}
                       onClick={() => openModal(guide.id)}
                       className="flex items-center gap-2 bg-white border-2 border-teal-100 hover:border-teal-400 text-teal-700 px-4 py-2.5 rounded-full font-medium transition-all shadow-sm hover:shadow active:scale-95"
                     >
                       {guide.icon}
                       {guide.title}
                     </button>
                   ))}
                 </div>
              </div>
            )}
          </div>

          {}
          <div className="space-y-6">
            <h3 className="text-2xl font-bold text-slate-800 flex items-center gap-2 border-b pb-2">
              <Heart className="text-rose-400" />
              Parenting Guide
            </h3>
            
            <div className="bg-rose-50 rounded-3xl p-6 border border-rose-100 shadow-sm space-y-6">
              
              <div>
                <h4 className="flex items-center gap-2 font-bold text-rose-800 mb-2">
                  <Utensils size={18} /> Feeding & Nutrition
                </h4>
                <p className="text-slate-700 text-sm leading-relaxed bg-white/60 p-3 rounded-xl">
                  {activeData.parenting.feeding}
                </p>
              </div>

              <div>
                <h4 className="flex items-center gap-2 font-bold text-indigo-800 mb-2">
                  <Moon size={18} /> Sleep Routines
                </h4>
                <p className="text-slate-700 text-sm leading-relaxed bg-white/60 p-3 rounded-xl">
                  {activeData.parenting.sleep}
                </p>
              </div>

              <div>
                <h4 className="flex items-center gap-2 font-bold text-emerald-800 mb-2">
                  <Star size={18} /> Suggested Activities
                </h4>
                <p className="text-slate-700 text-sm leading-relaxed bg-white/60 p-3 rounded-xl">
                  {activeData.parenting.activities}
                </p>
              </div>

            </div>
          </div>

        </div>
      </main>

      {}
      <div className="fixed bottom-0 left-0 w-full bg-white/80 backdrop-blur-md border-t border-slate-200 py-3 flex justify-center z-10">
        <div className="flex gap-1 sm:gap-2 overflow-x-auto px-4 max-w-full no-scrollbar pb-1">
          {availableMonths.map(m => (
            <button 
              key={m}
              onClick={() => setCurrentMonth(m)}
              className={`w-10 h-10 flex items-center justify-center rounded-full text-sm font-bold transition-all shrink-0 ${
                currentMonth === m 
                  ? 'bg-teal-500 text-white shadow-md scale-110' 
                  : 'bg-slate-100 text-slate-500 hover:bg-teal-100 hover:text-teal-700'
              }`}
            >
              {m >= 24 && m % 12 === 0 ? `${m/12}Y` : m}
            </button>
          ))}
        </div>
      </div>

      {/* Modal */}
      {activeModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/40 backdrop-blur-sm animate-in fade-in duration-200">
          <div 
            className="bg-white rounded-3xl shadow-2xl max-w-lg w-full max-h-[90vh] overflow-hidden flex flex-col transform scale-100 transition-transform"
            onClick={e => e.stopPropagation()}
          >
            <div className="flex justify-between items-center p-5 border-b border-slate-100 bg-teal-50/50">
              <h2 className="text-xl font-extrabold text-slate-800 flex items-center gap-2">
                <BookOpen className="text-teal-500" size={24} />
                {guideContent[activeModal]?.title}
              </h2>
              <button 
                onClick={closeModal}
                className="p-2 bg-white rounded-full text-slate-400 hover:text-rose-500 hover:bg-rose-50 transition-colors shadow-sm"
              >
                <X size={20} />
              </button>
            </div>
            <div className="p-6 overflow-y-auto custom-scrollbar">
              <p className="text-slate-600 leading-relaxed whitespace-pre-wrap text-[1.05rem]">
                {guideContent[activeModal]?.content}
              </p>
              
              {/* Optional dynamic prompt/disclaimer for specific modals */}
              {activeModal === 'psych-dev' && (
                <div className="mt-6 bg-amber-50 border border-amber-100 p-4 rounded-2xl text-sm text-amber-800 flex items-start gap-3">
                  <Info className="shrink-0 mt-0.5" size={18}/>
                  <p>These milestones align with developmental expectations outlined in standard frameworks. If you notice persistent delays across multiple domains, it is recommended to discuss them with your pediatrician.</p>
                </div>
              )}
            </div>
            <div className="p-4 border-t border-slate-100 bg-slate-50 flex justify-end">
               <button 
                 onClick={closeModal}
                 className="px-6 py-2 bg-slate-800 text-white font-semibold rounded-full hover:bg-slate-700 transition-colors"
               >
                 Close
               </button>
            </div>
          </div>
          
          {/* Invisible backdrop click catcher */}
          <div className="absolute inset-0 -z-10" onClick={closeModal}></div>
        </div>
      )}
      
      {/* Required CSS for hiding scrollbars but keeping functionality */}
      <style dangerouslySetInnerHTML={{__html: `
        .no-scrollbar::-webkit-scrollbar { display: none; }
        .no-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
        .custom-scrollbar::-webkit-scrollbar { width: 6px; }
        .custom-scrollbar::-webkit-scrollbar-track { background: transparent; }
        .custom-scrollbar::-webkit-scrollbar-thumb { background-color: #cbd5e1; border-radius: 10px; }
      `}} />
    </div>
  );
}
