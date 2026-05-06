#!/usr/bin/env python3
"""
GitHub Profile Stats Generator - 頁尾版本
安全地只更新頁尾的 Last Updated 時間戳
"""

import os
import re
from datetime import datetime

def update_readme():
    """
    安全地更新 README 頁尾的時間戳
    只修改最後的時間戳，不觸及其他內容
    """
    
    readme_path = 'README.md'
    
    # 檢查檔案是否存在
    if not os.path.exists(readme_path):
        print(f"❌ Error: {readme_path} not found!")
        return False
    
    try:
        # 讀取檔案
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 生成新的時間戳
        new_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
        
        # 模式 1: 尋找頁尾的時間戳（最後出現的時間戳）
        # 匹配格式如：Last Updated: YYYY-MM-DD HH:MM:SS UTC
        pattern = r'Last Updated: \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC'
        
        # 查找所有匹配
        matches = list(re.finditer(pattern, content))
        
        if not matches:
            print("⚠️  Warning: No 'Last Updated' timestamp found in README")
            print("   Please add this line to your footer:")
            print(f'   Last Updated: {new_timestamp}')
            return False
        
        # 只替換最後一個（頁尾的那個）
        last_match = matches[-1]
        old_timestamp = last_match.group()
        new_content = content[:last_match.start()] + f'Last Updated: {new_timestamp}' + content[last_match.end():]
        
        # 創建備份（以防萬一）
        import shutil
        backup_path = f"{readme_path}.backup"
        shutil.copy2(readme_path, backup_path)
        
        # 驗證重要內容還在（檢查關鍵標題）
        important_markers = [
            'About Me',
            'GitHub Stats',
            'Thank You',
            'Discord',
        ]
        
        missing = [m for m in important_markers if m not in new_content]
        if missing:
            print(f"❌ Error: Missing content markers: {missing}")
            print("   Reverting changes...")
            shutil.copy2(backup_path, readme_path)
            return False
        
        # 寫入新內容
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        # 輸出成功信息
        print("✅ SUCCESS!")
        print(f"   Old: {old_timestamp}")
        print(f"   New: Last Updated: {new_timestamp}")
        print(f"   Backup: {backup_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """主程式進入點"""
    print("-" * 70)
    print("GitHub Profile README Stats Updater - Footer Version")
    print("-" * 70)
    
    success = update_readme()
    
    print("-" * 70)
    if success:
        print("✨ Update completed successfully!")
    else:
        print("⚠️  Update failed. Please check the README format.")
    print("-" * 70)
    
    return 0 if success else 1

if __name__ == '__main__':
    exit(main())
