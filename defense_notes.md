# Medidas de Prevenção e Defesa contra Malware

Este documento apresenta as principais estratégias de defesa contra ameaças como Ransomware e Keyloggers, reforçando a importância da segurança em camadas e da conscientização dos usuários.

---

# Defesa contra Ransomware

O ransomware é um tipo de malware que sequestra arquivos por meio de criptografia, exigindo pagamento para a suposta liberação dos dados.

## Principais medidas de proteção

### Backup 3-2-1

Manter:
- 3 cópias dos dados
- 2 mídias diferentes
- 1 cópia offline ou offsite

Essa prática reduz drasticamente o impacto de ataques.

---

### MFA (Autenticação Multifator)

Mesmo com o comprometimento de senhas, o invasor encontra uma barreira adicional de acesso.

---

### Patch Management

Sistemas desatualizados são portas de entrada comuns para ataques.

Aplicar atualizações de segurança reduz significativamente a superfície de ataque.

---

### EDR / Antivírus

Ferramentas de Endpoint Detection and Response ajudam a identificar comportamentos suspeitos como:

- criptografia em massa
- movimentação lateral
- execução anômala de processos

---

### Segmentação de Rede

Evita a propagação rápida do ransomware entre servidores e estações.

---

### Anti-Phishing

Grande parte dos ataques começa com engenharia social.

Treinamento contínuo reduz esse risco.

---

# Defesa contra Keyloggers

Keyloggers são malwares utilizados para capturar teclas digitadas, geralmente com foco em roubo de credenciais.

## Principais medidas de proteção

### Antivírus com detecção comportamental

Nem todo keylogger é detectado por assinatura.

A análise comportamental aumenta a capacidade de defesa.

---

### MFA novamente

Mesmo com a senha capturada, o invasor ainda encontra dificuldade de acesso.

---

### Password Managers

Reduzem a necessidade de digitação manual de senhas, diminuindo a exposição.

---

### Sandboxing

Executar aplicações suspeitas em ambientes isolados reduz riscos.

---

### Hardening do Endpoint

Boas práticas como:

- desabilitar privilégios desnecessários
- controle de aplicações
- princípio do menor privilégio

aumentam a segurança.

---

### Conscientização do Usuário

O fator humano continua sendo uma das maiores superfícies de ataque.

Treinamento e awareness são indispensáveis.

---

# Conclusão

A melhor defesa não depende de uma única ferramenta, mas sim de uma estratégia de segurança em camadas.

Tecnologia, processos e pessoas precisam trabalhar juntos para reduzir riscos e fortalecer a postura de segurança da informação.