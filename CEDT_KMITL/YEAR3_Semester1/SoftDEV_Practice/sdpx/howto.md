## HOW TO GIT ##
    - Create Repo
    - Clone : git clone [link repo]
        - cd repo folder
            - (main) notepad member.txt
                - # B 
                    C 
                    D 
                    E
            - (main) git add .
            - (main) git commit -m "add member.txt"
            - (main) git push -u origin main
            - (main) git checkout -b dev
            - (dev) git push -u origin dev
            - (dev) git checkout -b b1

            - (b1) notepad member.txt
                - # B bb
                    C 
                    D 
                    E
            - (b1) git add .
            - (b1) git commit -m "Add b's name"
            - (b1) git push -u origin b1
            - (b1) git checkout dev

            - (dev) git checkout -b c1

            - (c1) notepad member.txt
                - # B 
                    C cc 
                    D 
                    E
            - (c1) git add .
            - (c1) git commit -m "add c' name"
            - (c1) git push -u origin c1
            - (c1) git checkout dev

            - (dev) git pull origin dev
            - (dev) git checkout b1

# สร้าง Pull request and Merging #
            - (b1) gh pr create --base dev
            - (b1) gh pr merge 1      #!! ตอนมันจะถามว่าจะลบ branch ไหม อย่ามือไวกด enter ให้ พิม N ย้ำ N เท่านั้น!! อย่าลืมพิมพ์ N !!!
            - (b1) git checkout c1

            - (c1) gh pr create --base dev   
            - (c1) gh pr merge 2                <--- จะเกิด Conflict #1
            - (c1) git checkout dev

            - (dev) git pull origin dev
            - (dev) git checkout c1

            - (c1) notepad member.txt
            - (c1) git add .
            - (c1) git commit -m "Fix: conflict"
            - (c1) git push -u origin c1
            - (c1) gh pr merge 2
            - (c1) git checkout dev

            - (dev) git pull origin dev

            - (dev) git checkout -b d1,e1 # วนลูปขึ้นไปข้างบน ทำซ้ำ d1 กับ e1

# After finish #
            - ไป dev branch
            - (dev) gh pr create --base main
            - (dev) gh pr merge 5

# END #