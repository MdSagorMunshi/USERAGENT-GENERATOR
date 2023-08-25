## Code Write By Md Sagor Munshi
## facebook.com/100000852187941

from fake_useragent import UserAgent

def save_user_agents_to_file(user_agents, filename):
    with open(filename, 'w') as file:
        file.write('\n'.join(user_agents))

if __name__ == "__main__":
    user_agent_generator = UserAgent()
    num_user_agents = 999999
    generated_user_agents = [user_agent_generator.random for _ in range(num_user_agents)]
    filename = "user_agents.txt"
    save_user_agents_to_file(generated_user_agents, filename)

    print(f"{num_user_agents} User-Agents generated and saved to {filename}:\n")
    for user_agent in generated_user_agents:
        print(user_agent)
