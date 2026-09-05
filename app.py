#!/usr/bin/env python3
"""
MIND'S EDGE: SCREENLESS AUDIO RPG SDE ENGINE
Version: 2.0.0 (Unified Stochastic & Semantic Density Edition)
--------------------------------------------------------------------------------
This master state-engine implements:
1. Stochastic Differential Equations (SDE) for signal decoherence:
   dX_t = theta * (mu - X_t) * dt + sigma * dW_t
2. Semantic Density Effect (SDE) and Semantic Isolation:
   Isolates raw float-level telemetry from the semantic rendering engine.
   As decoherence (X_t) spikes, the narrative "semantic density" increases,
   triggering linguistic fragmentation, nested sensory audio logs, and 
   increasingly complex haptic/sensor constraints.
--------------------------------------------------------------------------------
"""

import sys
import random
import math

class ScreenlessSDEEngine:
    def __init__(self):
        # 1. Core Mathematical Telemetry (Isolated from Semantics)
        self.stamina = 12.0
        self.cohesion = 10.0
        self.soot = 1.0  # 0 to 8 carrying slots occupied by lead oxide
        self.pacemaker_charges = 3
        self.scars = []
        
        # SDE Parameters
        self.x_t = 0.15  # Starting decoherence level (0.0 to 1.0)
        self.theta = 1.5  # Reversion speed (Arthur's antenna alignment strength)
        self.mu_base = 0.30  # Baseline noise equilibrium
        self.sigma_base = 0.25  # Volatility / turbulence base
        
        # Grid Tracking
        self.current_col = 10  # Col 'J'
        self.current_row = 1   # Row '1'
        self.turns_completed = 0
        self.endgame_row = 20  # Northern County Line F20 (Col 6, Row 20)
        self.is_terminal = False
        self.victory = False
        
        # Hardware Sensor Emulation
        self.mic_volume_db = 15.0
        self.ambient_light_lux = 1.5
        self.s_pen_velocity = 20.0  # m/s
        self.pencil_grade = "2B"  # Soft graphite grants Chroma Shielding

    def step_sde(self, steps, card_suit):
        """
        Solves the Ornstein-Uhlenbeck SDE numerically for one turn step.
        dX_t = theta * (mu - X_t) * dt + sigma * dW_t
        """
        # Delta Time is proportional to movement step distance
        dt = max(0.05, steps / 20.0)
        
        # Define stochastically shifting SDE coefficients based on Suit Modulation
        if card_suit == "Clubs":    # Resonant Feed
            mu = 0.25
            theta = 1.6
            sigma = self.sigma_base
        elif card_suit == "Spades":  # Static Flare (Unshielded)
            mu = 0.75
            theta = 1.0
            sigma = self.sigma_base + 0.15
        elif card_suit == "Hearts":  # Warmth Signal (Stable Loop)
            mu = 0.10
            theta = 2.0
            sigma = self.sigma_base - 0.10
        elif card_suit == "Diamonds": # Closed Circuit (Highly Volatile)
            mu = 0.45
            theta = 0.8
            sigma = self.sigma_base + 0.25
        else:
            mu = self.mu_base
            theta = self.theta
            sigma = self.sigma_base

        # Apply Pencil Graphite Carbon Shielding
        if self.pencil_grade in ["2B", "4B", "6B"]:
            sigma = max(0.05, sigma - 0.08)  # Thick carbon shields the line

        # Standard Brownian Motion Increment (Wiener Process)
        # Random normal sample using Box-Muller transform
        u1 = random.random()
        u2 = random.random()
        z = math.sqrt(-2.0 * math.log(max(1e-9, u1))) * math.cos(2.0 * math.pi * u2)
        dw = z * math.sqrt(dt)

        # Compute dX_t change
        dx = theta * (mu - self.x_t) * dt + sigma * dw
        
        # Update and clamp Decoherence
        self.x_t = max(0.0, min(1.0, self.x_t + dx))
        return self.x_t

    def calculate_scanline_steps(self, tremor, card_value):
        """Calculates Scanline Step count factoring in soot soot-friction."""
        return max(1, tremor + card_value + int(self.soot))

    def evaluate_semantic_density_effect(self):
        """
        IMPLEMENTS THE SEMANTIC DENSITY EFFECT (SDE) & SEMANTIC ISOLATION
        Translates raw float-level decoherence (self.x_t) into isolated linguistic 
        constructs that spike in textual and sensory density as sync degrades.
        """
        x = self.x_t
        
        # Category A: High-Fidelity/Clear Signal (0.0 <= X_t <= 0.25)
        if x <= 0.25:
            sensory_audio = "🔊 [AMBIENT] Liminal cornfield wind. The 15.734 kHz flyback whine softens to a clean, rhythmic tick."
            sensory_haptic = "💓 [HAPTIC] Stable, reassuring slow pulse [45 BPM, 10% Intensity]."
            narrative = (
                "The air is cold and smells faintly of winter rye. Your Zenith repair monitor shines a "
                "steady silver grid over the dirt walls of your silo. The pencil lines are sharp and unblurred."
            )
            mechanics = "RECOVERY ACTIVE: Locate a Sears parts locker to vacuum 1 unit of Soot."
            density_ratio = 1.0  # Baseline semantic density (clinical, sparse)
            
        # Category B: Tracking Drift (0.25 < X_t <= 0.55)
        elif x <= 0.55:
            sensory_audio = "🔊 [AMBIENT] Wind rising. | [SPATIAL - FRONT_LEFT] Low, periodic crackle of decaying tape."
            sensory_haptic = "💓 [HAPTIC] Accelerated heartbeat rhythm [65 BPM, 25% Intensity]."
            narrative = (
                "A thin, grease-scented layer of black polyurethane binder condenses on your headphones. "
                "The tracking lines hum in your throat. Your shadow remains aligned, but your boots feel heavy."
            )
            mechanics = "SIGNAL DISTORTION: S-Pen strike checks are normal. Watch your step vectors."
            density_ratio = 1.5  # Moderate density (sensory-layering starts)
            
        # Category C: High Chroma Distortion (0.55 < X_t <= 0.80)
        elif x <= 0.80:
            sensory_audio = (
                "🔊 [AMBIENT] Wind screams. | [SPATIAL - REAR_RIGHT] Servos of a Hollow Subaltern "
                "pulsing: guttural, wet metallic gurgling and motor whine (Proximity: 30.0%)."
            )
            sensory_haptic = "💓 [HAPTIC] Fast, fluttering panic pulse [95 BPM, 60% Intensity]. Phone vibrates with minor tremors."
            narrative = (
                "CHROMA BLEED. Horizontal tracking bars slice across the dirt walls. Your physical shadow "
                "detaches from your collarbone, lagging exactly three frames behind your body as a solid, "
                "impassable barrier of black static. A cold, wet rot seeps from the floorboards."
            )
            mechanics = "COMBAT PROTOCOL ENGAGED: S-Pen Swipe velocity threshold is standard (15.0 m/s). Fail = -2 Cohesion."
            density_ratio = 2.5  # Heavy density (linguistic fragmentation, sensory clutter)
            
        # Category D: Deflection Tear / Systemic Meltdown (0.80 < X_t <= 1.00)
        else:
            sensory_audio = (
                "🔊 [SYSTEM ERROR] High-frequency flyback scream (15.734 kHz) spikes to 95 dB. | "
                "[SPATIAL - EVERYWHERE] Blinding, crackling composite static sweeps your headset."
            )
            sensory_haptic = "⚠️ [HAPTIC] Continuous high-voltage electrical flutter [145 BPM, 90% Intensity]. Somatic lockout hazard."
            narrative = (
                "DEFLECTION COLLAPSE. THE GREEN PHOSPHOR LAYER OF THE ATMOSPHERE TEARS OPEN. "
                "consensus reality dissolves into a flat, green vector line. Arthur's transmitter discharges "
                "50,000 volts of raw back-emf current directly into your chest wires. Your skin smells of melting "
                "plastic and ozone. The static-choked dead are crawling through the monitor glass."
            )
            mechanics = "CRITICAL FAIL: Pacemaker fuses blowing! Suffer 3 Stamina damage and mark a permanent SOLDER BURN."
            density_ratio = 4.0  # Extreme density (chaotic, capital letters, sensory overload)
            
        return {
            "x_t": x,
            "sensory_audio": sensory_audio,
            "sensory_haptic": sensory_haptic,
            "narrative": narrative,
            "mechanics": mechanics,
            "density_ratio": density_ratio
        }

    def process_turn(self, card_suit, card_value, d6_tremor):
        """Processes one complete simulation turn."""
        self.turns_completed += 1
        
        # 1. Environmental Sensor Checks (Emulated physical inputs)
        if self.turns_completed == 2:
            self.mic_volume_db = 65.0  # Emulate real-world stealth fail (loud decibel spike)
            self.ambient_light_lux = 1.2
        else:
            self.mic_volume_db = random.uniform(10.0, 20.0)
            self.ambient_light_lux = random.uniform(0.0, 2.5)

        # 2. S-Pen Swing Check (Combat simulation if decoherence is high)
        if self.x_t > 0.55:
            # S-Pen swipe check
            threshold = 30.0 if "SHATTERED" in self.scars else 15.0
            self.s_pen_velocity = random.uniform(8.0, 25.0)  # m/s
            swipe_success = self.s_pen_velocity >= threshold
        else:
            swipe_success = True

        # 3. Calculate steps and run SDE
        steps = self.calculate_scanline_steps(d6_tremor, card_value)
        
        # Spades penalty
        if card_suit == "Spades":
            self.soot = min(8.0, self.soot + 1.0)
            self.cohesion = max(0.0, self.cohesion - 1.0)
            
        # Hearts recovery
        if card_suit == "Hearts":
            self.stamina = min(12.0, self.stamina + 1.0)
            self.cohesion = min(10.0, self.cohesion + 1.0)

        # Step SDE Solver
        self.step_sde(steps, card_suit)

        # Move coordinates Northward toward the target border
        self.current_row = min(20, self.current_row + int(steps // 2))
        self.current_col = min(20, max(1, self.current_col + int(steps % 3) - 1))
        current_coord = f"{chr(64 + self.current_col)}{self.current_row}"

        # 4. Handle SDE Hazards & Resolving Overwrites
        collision_trigger = False
        mishap_type = None
        
        # Mic decibel spike alerts anomalies
        if self.mic_volume_db > 40.0:
            collision_trigger = True
            mishap_type = "MIC_STEALTH_FAILURE"
            
        # SDE Decoherence above 0.75 triggers a natural tracking collision
        if self.x_t > 0.75 and not collision_trigger:
            collision_trigger = True
            mishap_type = "DEFLECTION_TEAR_COLLISION"

        # Overwrite Traceback Resolution (Fate Mill d20)
        overwrite_log = ""
        if collision_trigger:
            fate_roll = random.randint(1, 20)
            
            # Apply modifiers
            if "SHATTERED" in self.scars:
                fate_roll -= 2  # Battered body makes rubbing out lines clumsy
            
            if fate_roll == 20:
                self.soot = max(0.0, self.soot - 1.0)
                overwrite_log = "FATE d20 [20] - PERFECT OVERWRITE. Erased path successfully. Reclaim 1 lung slot."
            elif 13 <= fate_roll <= 19:
                self.soot = min(8.0, self.soot + 1.0)
                overwrite_log = "FATE d20 [13-19] - OVERWRITE COMPROMISED. Erased, but soot caked lung slots by +1."
            elif 10 <= fate_roll <= 12:
                if self.pacemaker_charges > 0:
                    self.pacemaker_charges -= 1
                    overwrite_log = f"FATE d20 [10-12] - COERCIVITY LOCK. Spent 1 Pacemaker charge (Fuses: {self.pacemaker_charges}/3)."
                else:
                    self.stamina = max(0.0, self.stamina - 3.0)
                    overwrite_log = "FATE d20 [10-12] - COERCIVITY LOCK. No fuses left! Suffer hard 3 Stamina shock."
            else:
                self.stamina = max(0.0, self.stamina - 3.0)
                self.pacemaker_charges = max(0, self.pacemaker_charges - 1)
                # Welded Solder Burn
                overwrite_log = f"FATE d20 [1-9] - CATASTROPHIC COLLAPSE. Pacemaker blown. Suffer 3 Stamina damage and +1 permanent Solder Burn."
                
            # Combat resolution
            if not swipe_success:
                self.cohesion = max(0.0, self.cohesion - 2.0)
                overwrite_log += " | COMBAT CHECK FAILED: S-Pen Swipe velocity was too low. Took 2 Cohesion damage."

        # 5. Check "Broken" Trauma Conditions
        broken_log = ""
        if self.stamina <= 0.0 and "SHATTERED" not in self.scars:
            # Choose to mark "SHATTERED" Scar to survive once
            self.scars.append("SHATTERED")
            self.stamina = 6.0
            broken_log = "⚠️ [TRAUMA EVENT] Stamina hit 0! You bypass terminal death by marking the permanent 'SHATTERED' SCAR (-1 Strength)."
        elif self.stamina <= 0.0:
            self.is_terminal = True
            broken_log = "💀 [TERMINAL DEATH] Physical collapse. Your pacemaker has flatlined in the clay."
            
        if self.soot >= 8.0:
            self.is_terminal = True
            broken_log = "💀 [TERMINAL DEATH] Ashen suffocation. Your carrying ledger is completely choked with lead soot."

        if self.cohesion <= 0.0:
            self.is_terminal = True
            broken_log = "💀 [TERMINAL DEATH] Psychosis. Your mind has desynchronized completely from consensus reality."

        # Endgame Check
        if self.current_row >= self.endgame_row and not self.is_terminal:
            self.is_terminal = True
            self.victory = True

        # Render Semantic Projection
        projection = self.evaluate_semantic_density_effect()
        
        # Display formatted output
        print(f"================================================================================")
        print(f" [TURN {self.turns_completed:02d}] POSITION: {current_coord} | STAMINA: {self.stamina}/12 | COHESION: {self.cohesion}/10")
        print(f"--------------------------------------------------------------------------------")
        print(f" 🎛️  [HARDWARE SENSORS] Mic Volume: {self.mic_volume_db:.1f} dB | Ambient Light: {self.ambient_light_lux:.1f} Lux")
        print(f"  [SDE SOLVER] Steps formula: S = d({d6_tremor}) + c({card_value}) + Soot({int(self.soot)}) - Pencil(3) = {steps} SQUARES")
        print(f"  [SDE SOLVER] Continuous Decoherence Level (X_t): {projection['x_t']:.4f} (Density Factor: {projection['density_ratio']:.1f}x)")
        print(f"")
        print(f" {projection['sensory_audio']}")
        print(f" {projection['sensory_haptic']}")
        print(f" ✍️  [NARRATIVE PROJECTION] {projection['narrative']}")
        
        if card_suit == "Spades":
            print(f"  [♠️ CARD ATTRITION] Unshielded Spades degrade Cohesion by -1 and add +1 Soot.")
        elif card_suit == "Hearts":
            print(f"  [♥️ CARD FEEDBACK] Warmth Signal feedback restores +1 Stamina, +1 Cohesion.")
            
        if collision_trigger:
            print(f"  [⚠️ MISHAP TRIGGERED: {mishap_type}]")
            print(f"  [FATE RESOLUTION] {overwrite_log}")
            
        if broken_log:
            print(f"  {broken_log}")
            
        print(f"================================================================================")
        print()

def simulate_campaign():
    print("================================================================================")
    print("                 S26 ULTRA COMPLIANCE: SCREENLESS AUDIO ENGINE                  ")
    print("               STOCHASTIC & SEMANTIC DENSITY EXPEDITION RUN                     ")
    print("================================================================================")
    print("🔊 [Earbuds] 'Safe Zone connection broken. Entering Sector 4: Mind's Edge.'")
    print("💓 [Haptics] Transitioning to erratic ambient heartbeat vibration...")
    print("--------------------------------------------------------------------------------\n")
    
    engine = ScreenlessSDEEngine()
    
    # Pre-drafted cards representing Tommy's 5-Act tragic run
    turns_deck = [
        ("Clubs", 5, 3),    # Turn 1: Easy baseline
        ("Spades", 10, 4),   # Turn 2: Sound spike stealth failure
        ("Spades", 8, 2),    # Turn 3: Continuing through Spades
        ("Spades", 12, 5),   # Turn 4: High tension tracking crash
        ("Hearts", 6, 2),    # Turn 5: Warm signal recovery
    ]
    
    for suit, val, tremor in turns_deck:
        if engine.is_terminal:
            break
        engine.process_turn(suit, val, tremor)
        
    if engine.victory:
        print("\n🏆 [FEEDBACK LOG] TARGET COUNTY BOUNDARY REACHED.")
        print("🔊 [Earbuds] 'Ground carrier signal locked. Snapping physical Write-Protect Tab.'")
        print("✂️  [PHYSICAL ACTION REQUIRED] Cut off left shoulder tab of your map card.")
        print("================================================================================")
    elif engine.is_terminal:
        print("\n💀 [SYSTEM COLLAPSE] LOOP ENDS IN THE SOOT-CLAY.")
        print("🔊 [Earbuds] 'Sync lock lost... Static taking over... Goodbye...'")
        print("================================================================================")

if __name__ == "__main__":
    simulate_campaign()
