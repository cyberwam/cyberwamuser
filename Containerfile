FROM archlinux
RUN echo y | pacman -Syu python3
RUN useradd -m user
RUN chown user:user /home/user
RUN mkdir -p /home/user/.config

USER user

RUN echo "source /home/user/cyberwamuser/venv/bin/activate" >> /home/user/.bashrc
WORKDIR /home/user/cyberwamuser
COPY --chown=user:user cyberwamuser .
COPY --chown=user:user requirements.txt .
COPY --chown=user:user tmp/service /home/user/.config/cyberwamuser/service
COPY --chown=user:user tmp/agent.json /home/user/.config/cyberwamuser/agent.json
RUN python3 -m venv venv && ./venv/bin/pip install -r requirements.txt
