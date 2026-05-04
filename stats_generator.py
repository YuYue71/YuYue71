#!/usr/bin/env python3
"""
GitHub Profile Stats Generator
自動生成和更新 GitHub 個人檔案的統計數據
"""

import os
import re
from datetime import datetime

def generate_stats():
    """生成統計數據的 Markdown 內容"""
    
    # 這裡可以集成真實的 GitHub API 調用來獲取最新數據
    # 目前使用靜態卡片 URL（使用 github-readme-stats 服務）
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
    
    stats_content = f"""<!-- 訪客計數器 -->
<div align="center">
  <img src="https://komarev.com/ghpvc/?username=YuYue71&style=for-the-badge&color=0d1117&labelColor=181824" alt="Profile Views" />
</div>

<!-- 上次更新時間 -->
<div align="center">
  <sub>Last Updated: {timestamp}</sub>
</div>
"""
    
    return stats_content

def update_readme(stats):
    """更新 README 文件中的統計部分"""
    
    readme_path = 'README.md'
    
    if not os.path.exists(readme_path):
        print(f"❌ {readme_path} not found!")
        return False
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 查找統計區域的標記
    # 在第一個 <!-- 訪客計數器 --> 和下一個 --- 之間更新
    pattern = r'(<!-- 訪客計數器 -->.*?)(---)'
    
    replacement = stats + '\n\n$2'
    
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    # 驗證替換是否成功
    if new_content == content:
        print("⚠️  No stats section found to update. Please check the README format.")
        return False
    
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("✅ README.md updated successfully!")
    print(f"   Updated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    return True

def main():
    """主函數"""
    print("🔄 Starting GitHub Profile Stats Update...")
    print("-" * 50)
    
    try:
        # 生成統計數據
        stats = generate_stats()
        
        # 更新 README
        if update_readme(stats):
            print("✨ Profile update completed successfully!")
        else:
            print("⚠️  Update completed with warnings.")
            
    except Exception as e:
        print(f"❌ Error occurred: {e}")
        return 1
    
    return 0

if __name__ == '__main__':
    exit(main())
  
