def register_routes(app):
    from app.routes.main_routes import main_bp
    from app.routes.save_routes import save_bp
    from app.routes.user_routes import user_bp
    from app.routes.verse_routes import verse_bp
    from app.routes.feature_route import feature_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(save_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(verse_bp)
    app.register_blueprint(feature_bp)


    
    
    
