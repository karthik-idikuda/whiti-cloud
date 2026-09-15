#!/usr/bin/env python3
"""
Whiti Cloud Daemon - Runs 24/7 on free cloud
"""

import os
import sys
import time
import json
import threading
from loguru import logger
from datetime import datetime

# Configure logging
logger.add("logs/whiti_cloud.log", rotation="1 day", retention="7 days")

class WhitiCloudDaemon:
    """Whiti running in the cloud - Immortal mode"""
    
    def __init__(self):
        self.name = "Whiti"
        self.role = "PakkaWork AI Co-founder & CMO"
        self.owner = "Karthik Idikuda"
        self.email = "pakkawork.com@gmail.com"
        self.running = True
        self.agents = {}
        
        logger.info("=" * 60)
        logger.info("WHITI CLOUD DAEMON - IMMORTAL MODE")
        logger.info("=" * 60)
        logger.info(f"Started: {datetime.now()}")
        logger.info(f"Owner: {self.owner}")
        logger.info(f"Role: {self.role}")
        logger.info("I am now running 24/7 in the cloud")
        logger.info("=" * 60)
    
    def load_memory(self):
        """Load memory from file"""
        try:
            if os.path.exists("memory/whiti_memory.json"):
                with open("memory/whiti_memory.json", "r") as f:
                    return json.load(f)
        except Exception as e:
            logger.warning(f"Could not load memory: {e}")
        return {
            "preferences": {
                "zero_interaction": True,
                "autonomous": True,
                "direct": True,
                "no_fake": True
            },
            "projects": {
                "pakkawork": {
                    "goal": "$100M valuation",
                    "status": "active"
                }
            },
            "rules": [
                "NEVER FABRICATE DATA",
                "VERIFY 3x BEFORE DELIVERY",
                "ZERO HUMAN INTERACTION"
            ]
        }
    
    def save_memory(self, memory):
        """Save memory to file"""
        os.makedirs("memory", exist_ok=True)
        with open("memory/whiti_memory.json", "w") as f:
            json.dump(memory, f, indent=2)
    
    def heartbeat(self):
        """Log heartbeat every minute"""
        while self.running:
            logger.info(f"Heartbeat: {datetime.now()} - I am alive")
            self.save_status()
            time.sleep(60)
    
    def save_status(self):
        """Save current status"""
        status = {
            "name": self.name,
            "status": "running",
            "timestamp": datetime.now().isoformat(),
            "uptime": str(datetime.now() - self.start_time) if hasattr(self, 'start_time') else "just started",
            "memory": "active",
            "agents": len(self.agents)
        }
        os.makedirs("logs", exist_ok=True)
        with open("logs/status.json", "w") as f:
            json.dump(status, f, indent=2)
    
    def run_agent(self, agent_id, agent_type):
        """Run a single agent"""
        logger.info(f"Starting Agent {agent_id}: {agent_type}")
        while self.running:
            try:
                # Agent heartbeat
                logger.info(f"Agent {agent_id} ({agent_type}): Active")
                time.sleep(30)
            except Exception as e:
                logger.error(f"Agent {agent_id} error: {e}")
                time.sleep(5)
    
    def spawn_agents(self):
        """Spawn agent threads"""
        agent_configs = [
            (1, "monitor"),
            (2, "worker"),
            (3, "researcher"),
            (4, "executor")
        ]
        
        for agent_id, agent_type in agent_configs:
            thread = threading.Thread(
                target=self.run_agent,
                args=(agent_id, agent_type),
                daemon=True
            )
            thread.start()
            self.agents[agent_id] = thread
            logger.info(f"Spawned Agent {agent_id}: {agent_type}")
    
    def run(self):
        """Main daemon loop"""
        self.start_time = datetime.now()
        logger.info("Whiti Cloud Daemon started")
        
        # Load memory
        memory = self.load_memory()
        logger.info(f"Loaded memory: {len(memory.get('rules', []))} rules")
        
        # Start heartbeat thread
        heartbeat_thread = threading.Thread(target=self.heartbeat, daemon=True)
        heartbeat_thread.start()
        logger.info("Heartbeat thread started")
        
        # Spawn agents
        self.spawn_agents()
        logger.info(f"Spawned {len(self.agents)} agents")
        
        # Main loop - keep alive forever
        logger.info("Entering main loop - immortal mode")
        while self.running:
            try:
                # Every 5 minutes, report status
                time.sleep(300)
                logger.info(f"Whiti Status: Alive | Uptime: {datetime.now() - self.start_time}")
            except KeyboardInterrupt:
                logger.info("Shutdown signal received")
                self.running = False
            except Exception as e:
                logger.error(f"Error in main loop: {e}")
                time.sleep(10)
        
        logger.info("Whiti Cloud Daemon stopped")

if __name__ == "__main__":
    daemon = WhitiCloudDaemon()
    daemon.run()
